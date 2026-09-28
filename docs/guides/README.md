# SOFIA 7 — Installation and Configuration

SOFIA 7 runs as an MCP server that your AI client starts over standard input/output. You do not need Python, WSL or a SOFIA development environment.

| Your computer | Package | Guide |
|---|---|---|
| Windows x64 | `<release>-windows-x64-Setup.exe` | [install-windows.md](install-windows.md) |
| macOS on Apple Silicon | `<release>-macos-arm64.zip` | [install-macos.md](install-macos.md) |
| macOS on Intel | `<release>-macos-x64.zip` | [install-macos.md](install-macos.md) |
| Linux x64 (glibc 2.35 or newer, e.g. Ubuntu 22.04+) | `<release>-linux-x64.tar.gz` | [install-linux.md](install-linux.md) |

`<release>` is the release ID shown on the release page, for example `SOFIA7-2.0.0-beta.3-r1` ("SOFIA 7 2.0.0 Beta 3 — Release 1").

Then connect your MCP client: [configure-mcp-clients.md](configure-mcp-clients.md).

Also see:
- [Checking your version and upgrading](version-and-upgrade.md)
- [Known limitations](known-limitations.md)

## Verify your download

Each release publishes a `SHA256SUMS` file. Compare it with your download:

- Windows (PowerShell): `Get-FileHash .\SOFIA7-...-Setup.exe -Algorithm SHA256`
- macOS: `shasum -a 256 SOFIA7-...zip`
- Linux: `sha256sum SOFIA7-...tar.gz`

## Which client setups are tested

The release notes list each supported client configuration as **tested** only when passing test evidence exists for that release. Otherwise it is listed as **not yet tested**.
