# Known limitations

- **WSL2 with the Windows executable:** projects must be on a Windows drive (`/mnt/<drive>/...`). Projects that exist only in the WSL Linux file system are not handled correctly yet; this is being addressed in SOFIA 7 itself.
- **Unsigned evaluation builds:** Windows may show a SmartScreen warning, and macOS requires removing the quarantine attribute (see [install-macos.md](install-macos.md)). Always check the published SHA-256 checksum first.
- **Linux baseline:** the Linux build needs glibc 2.35 or newer.
- **Linux build inside WSL2:** expected to work, but not tested or supported in this milestone.
- **WSL1:** not supported.
- **No automatic updates:** upgrade manually (see [version-and-upgrade.md](version-and-upgrade.md)).
