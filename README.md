# SOFIA 7

Official download channel for **SOFIA 7**, an engineering-method assistant that runs as an MCP server for AI clients such as Claude Code.

## Downloads

Releases are published on this repository's **Releases** page. Each release provides:

- a Windows x64 installer, macOS (Apple Silicon and Intel) `.zip` archives, and a Linux x64 `.tar.gz`
- `SHA256SUMS` to verify your download
- `release-manifest.json` identifying exactly which SOFIA 7 source revision each package was built from
- release notes listing which client configurations were tested for that release

No releases have been published yet.

## Installation and configuration

See [docs/guides](docs/guides/README.md).

## How releases are published

Releases are built, verified and assembled in a separate private pipeline and staged here as drafts. The [publish workflow](.github/workflows/publish.yml) makes a draft public only after the release approver approves it; it re-checks every file against its checksum first and records the approval with the release. Published releases are never modified.
