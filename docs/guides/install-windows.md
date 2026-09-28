# Installing SOFIA 7 on Windows x64

1. Download `<release>-windows-x64-Setup.exe` and check its SHA-256 (see [README.md](README.md)).
2. Run it. Administrator rights are required because SOFIA 7 installs to `C:\Program Files\SOFIA 7\`.
3. Accept the evaluation terms and finish the installer.

Evaluation builds are not code-signed yet, so Windows SmartScreen may warn about an unrecognized app. Choose **More info → Run anyway** only if the file's checksum matches the published `SHA256SUMS`.

## What gets installed where

| Location | Contents | Removed by uninstall? |
|---|---|---|
| `C:\Program Files\SOFIA 7\` | `sofia7.exe`, its `_internal\` folder, `build-identity.json`, notices, terms, these guides | Yes |
| `%LOCALAPPDATA%\SOFIA 7\` | SOFIA 7 settings and project registry | No |
| `%USERPROFILE%\Documents\SOFIA 7\` | Your projects and samples | No |

Next: [connect your MCP client](configure-mcp-clients.md).
