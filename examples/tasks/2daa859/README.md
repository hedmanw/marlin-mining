# 2daa859
- Result commit: [2daa85918ef297105bea73d006446339587eee8e](https://github.com/MarlinFirmware/Marlin/commit/2daa85918ef297105bea73d006446339587eee8e)
- First parent (base): [aba67e244922d8c71e26a215c06752c36743ae37](https://github.com/MarlinFirmware/Marlin/commit/aba67e244922d8c71e26a215c06752c36743ae37)
- Second parent (remote): [2015989f84918810be615deb57ad3baf9f66c203](https://github.com/MarlinFirmware/Marlin/commit/2015989f84918810be615deb57ad3baf9f66c203)

## Task
Merge _base_ with _remote_.
This task contains two files to merge: `Marlin_main.cpp` and `ultralcd.cpp`.

In general, the remote should be integrated as evolution. There are some exceptions to this in `Marlin_main.cpp` and `ultralcd.cpp`.

`Marlin_main.cpp`, context `process_commands()`:
* From `base`, the new content for `case 80:` should be kept.
* From `base`, the new content for `case 81:` should be kept.

`ultralcd.cpp`, context `lcd_prepare_menu()`:
* From `base`, the new content `if (powersupply) [...]` should be kept.
