# Installing SOFIA 7 on macOS

Use `macos-arm64` on Apple Silicon Macs and `macos-x64` on Intel Macs.

1. Download the `.zip` for your Mac and check its SHA-256 (see [README.md](README.md)).
2. Extract it to a permanent location, for example:

   ```sh
   mkdir -p ~/Applications
   cd ~/Applications
   ditto -x -k ~/Downloads/<release>-macos-arm64.zip .
   ```

3. Evaluation builds are not yet signed or notarized, so macOS Gatekeeper blocks them when they were downloaded with a browser. After checking the checksum, remove the quarantine attribute from the extracted folder:

   ```sh
   xattr -dr com.apple.quarantine ~/Applications/<release>-macos-arm64
   ```

4. Check that it runs:

   ```sh
   ~/Applications/<release>-macos-arm64/sofia7 --help
   ```

SOFIA 7 keeps its settings in `~/.local/share/SOFIA 7/` and your projects in `~/Documents/SOFIA 7/`. Both survive upgrades.

Next: [connect your MCP client](configure-mcp-clients.md).
