# Connecting an MCP client to SOFIA 7

SOFIA 7 is started by your MCP client as a **stdio** server with the argument `mcp`. It does not depend on a particular AI model or client. Claude Code is the reference client for this milestone; the examples below use it.

Whether a configuration is *tested* for a release is stated in that release's notes.

## Windows — Claude Code running natively on Windows (CFG-2)

```powershell
claude mcp add --scope user sofia7 -- "C:\Program Files\SOFIA 7\sofia7.exe" mcp
```

## Windows — Claude Code running inside WSL2 (CFG-1, reference configuration)

Install SOFIA 7 with the **Windows** installer, then register the Windows executable from inside WSL2. WSL2's Windows interoperability starts it:

```sh
claude mcp add --scope user sofia7 -- "/mnt/c/Program Files/SOFIA 7/sofia7.exe" mcp
```

- Keep the quotes: the path contains spaces.
- Windows interoperability must be enabled in WSL2 (it is by default).
- **Projects must live on a Windows drive**, i.e. under `/mnt/c/...` (or another `/mnt/<drive>/`). Projects stored only in the WSL Linux file system (such as `/home/you/project`) are not supported with this setup yet.
- Environment variables set in WSL are not passed to Windows programs unless they are listed in `WSLENV`. If you set `SOFIA7_APP_STATE_DIR` or `SOFIA7_WORKSPACE_DIR`, add them to `WSLENV` with the `/p` flag, e.g. `export WSLENV=$WSLENV:SOFIA7_WORKSPACE_DIR/p`.
- WSL1 is not supported.

## macOS (CFG-3, CFG-4)

```sh
claude mcp add --scope user sofia7 -- ~/Applications/<release>-macos-arm64/sofia7 mcp
```

Use the `macos-x64` folder on an Intel Mac.

## Linux (CFG-5)

```sh
claude mcp add --scope user sofia7 -- ~/.local/opt/<release>-linux-x64/sofia7 mcp
```

## Other MCP clients

Any MCP client that supports stdio servers can be configured with:

- command: the full path to `sofia7` (`sofia7.exe` on Windows)
- arguments: `mcp`

Other clients are not tested in this milestone.

## Checking the connection

In Claude Code, run `/mcp`; `sofia7` should be listed as connected. Asking the assistant to run the `sofia_health_check` tool should return `status: ok`.
