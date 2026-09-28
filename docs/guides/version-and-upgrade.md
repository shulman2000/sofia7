# Checking your version and upgrading

## Which version is installed?

Every package contains `build-identity.json` next to the `sofia7` executable (on Windows: `C:\Program Files\SOFIA 7\build-identity.json`). It records:

- `product_version` — the SOFIA 7 version
- `release_id` — the release, e.g. `SOFIA7-2.0.0-beta.3-r1` (its display name is "SOFIA 7 2.0.0 Beta 3 — Release 1"), or `SOFIA7-<version>-dev.<commit>` for development builds
- `build_kind` — `release_candidate` for approved releases, `development` for test builds that are never released
- `source` — exactly what it was built from: the requested reference and its type (tag or commit), the tags at that commit, and the full commit SHA
- `target` and `architecture`

## Upgrading (manual)

Automatic updates are not available yet.

- **Windows:** run the new installer. It upgrades the existing installation in place.
- **macOS / Linux:** extract the new archive next to the old one, update the path in your MCP client configuration, then delete the old folder.

Your settings and projects are stored outside the installation folder and are kept across upgrades. Restart your MCP client after upgrading.
