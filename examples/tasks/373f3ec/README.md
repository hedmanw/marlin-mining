# 373f3ec
- Result commit: [373f3ecab3ea9cb18d83d1899e7ff33cd515b0eb](https://github.com/MarlinFirmware/Marlin/commit/373f3ecab3ea9cb18d83d1899e7ff33cd515b0eb)
- First parent (mainline): [e36d31a3b7b699324d38d4b6d60d9e8ec638c114](https://github.com/MarlinFirmware/Marlin/commit/e36d31a3b7b699324d38d4b6d60d9e8ec638c114)
- Second parent (fork): [9e7b5056a0a02921d1e31d511b34efc9732e3c88](https://github.com/MarlinFirmware/Marlin/commit/9e7b5056a0a02921d1e31d511b34efc9732e3c88)

## Task
Instructions: Merge _mainline_ with _fork_.

Domain description: This replays the merge commit where Jcrocholl's deltabot functionality was integrated into the marlin mainline.
The mainline expects the 3D-printers to operate with a carthesian coordinate system.
The fork instead expects Delta printers, that operate on the relative difference between points, hence the name delta.

Integration instructions: There has been significant evolution in the Mainline, which should be accepted.
The functionality for movement should be integrated as follows:

* In `process_commands()`, under `case 28:`, inside the `QUICK_HOME` feature, accept the `fork` changes adding `current_position[n] = destination[n]`.
* The function `calculateDelta()` should be part of a `DELTA` feature.
* In the function `prepareMove()`, the differences between `mainline` and `fork` should be exclusive in a `DELTA` feature.
