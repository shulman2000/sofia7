"""Publish a staged draft release in the public sofia7 repository.

Runs in sofia7's publish workflow, inside the GitHub Environment "release"
(the release approver is the required reviewer). Self-contained and public:
it receives no private data and imports nothing from the private pipeline.

Steps: confirm the release is still a draft; download its assets; re-check every
package against SHA256SUMS and release-manifest.json; record the environment
approval as release-authorization.json; publish the draft. It never replaces an
asset of, or republishes, an already published release.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

REQUIRED = ("SHA256SUMS", "release-manifest.json", "RELEASE-NOTES.md", "evidence-summary.json")


def gh(*args: str, capture: bool = True) -> str:
    proc = subprocess.run(["gh", *args], capture_output=capture, text=True)
    if proc.returncode != 0:
        raise SystemExit(f"gh {' '.join(args[:3])} failed: {proc.stderr}")
    return proc.stdout


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def check_assets(folder: Path) -> dict:
    """Return the manifest if every package matches SHA256SUMS and the manifest; otherwise exit."""
    missing = [n for n in REQUIRED if not (folder / n).is_file()]
    if missing:
        raise SystemExit(f"draft is missing {missing}")
    manifest = json.loads((folder / "release-manifest.json").read_text(encoding="utf-8"))
    sums = dict(reversed(line.split("  ", 1)) for line in (folder / "SHA256SUMS").read_text().splitlines() if line)
    problems = []
    for pkg in manifest["packages"]:
        path = folder / pkg["file_name"]
        if not path.is_file():
            problems.append(f"{pkg['file_name']} missing")
        elif not (sha256(path) == pkg["sha256"] == sums.get(pkg["file_name"])):
            problems.append(f"{pkg['file_name']} checksum mismatch")
    if problems:
        raise SystemExit("refusing to publish: " + "; ".join(problems))
    return manifest


def authorization_record(approvals: list[dict], release_id: str, manifest_digest: str) -> dict:
    for approval in approvals:
        envs = {e.get("name") for e in approval.get("environments", [])}
        if approval.get("state") == "approved" and "release" in envs:
            return {
                "kind": "release_authorization",
                "subject": f"{release_id}@sha256:{manifest_digest}",
                "decision": "approved",
                "approver": approval["user"]["login"],
                "decided_at": approval.get("submitted_at") or approval.get("created_at", ""),
                "comment": approval.get("comment", ""),
            }
    raise SystemExit("no approval of the 'release' environment recorded for this run")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--release-id", required=True)
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()

    info = json.loads(gh("release", "view", args.release_id, "--repo", args.repo, "--json", "isDraft,tagName"))
    if not info["isDraft"]:
        raise SystemExit(f"{args.release_id} is already published; published releases are immutable")
    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp)
        gh("release", "download", args.release_id, "--repo", args.repo, "--dir", str(folder))
        manifest = check_assets(folder)
        if manifest["release_id"] != args.release_id:
            raise SystemExit("manifest release_id does not match the draft")
        approvals = json.loads(gh("api", f"repos/{args.repo}/actions/runs/{args.run_id}/approvals"))
        record = authorization_record(approvals, args.release_id, sha256(folder / "release-manifest.json"))
        auth = folder / "release-authorization.json"
        auth.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        gh("release", "upload", args.release_id, str(auth), "--repo", args.repo)
    gh("release", "edit", args.release_id, "--repo", args.repo, "--draft=false")
    print(f"published {args.release_id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
