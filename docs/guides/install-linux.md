# Installing SOFIA 7 on Linux x64

Requires glibc 2.35 or newer (for example Ubuntu 22.04+, Debian 12+, RHEL 10). Check with `ldd --version`.

1. Download `<release>-linux-x64.tar.gz` and check its SHA-256 (see [README.md](README.md)).
2. Extract it to a permanent location:

   ```sh
   mkdir -p ~/.local/opt
   tar -xzf ~/Downloads/<release>-linux-x64.tar.gz -C ~/.local/opt
   ```

3. Check that it runs:

   ```sh
   ~/.local/opt/<release>-linux-x64/sofia7 --help
   ```

SOFIA 7 keeps its settings in `~/.local/share/SOFIA 7/` and your projects in `~/Documents/SOFIA 7/`. Both survive upgrades.

Using WSL2 on Windows? The recommended setup is the **Windows** installer, launched from WSL2 (see [configure-mcp-clients.md](configure-mcp-clients.md)). Running this Linux build inside WSL2 is expected to work but is not tested or supported in this milestone.

Next: [connect your MCP client](configure-mcp-clients.md).
