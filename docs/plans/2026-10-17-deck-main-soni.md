# Steam Deck integration implementation plan

Goal: install a native Linux build combining upstream main, Hugo PRs 94/100 and soni424 main.

Architecture: retain the merged renderer/runtime and launcher features; apply PR72 Linux build support and a Linux runner path in the launcher. Build in an isolated WSL checkout with GCC14 and existing static dependencies. Deploy a versioned package with rollback while retaining user data and settings.

1. Merge upstream b787c10, both PR heads, soni424 e19e2c3; resolve duplicated cherry-picks using the soni implementations.
2. Apply Linux PR72; retain all soni features and add Linux launcher execution support.
3. Use local version 0.3.6.2; preserve saves, game paths, FPS choice, MAKO and Steam entry.
4. Compile under WSL Ubuntu with GCC14, LTO off and PGO off.
5. Run targeted launcher/runtime tests, check dependencies and shader compilation.
6. Package launcher/scripts/runtime/library and deployment provenance without game data.
7. Back up the working Deck installation, deploy, validate hashes and launch via Steam.
8. Verify actual rendering and kernel/device-loss logs; report remaining gameplay validation limits.

Do not change or push the independent PR branches. Keep installed game data and user saves intact.
