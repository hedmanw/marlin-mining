# 373f3ec
- Result commit: [373f3ecab3ea9cb18d83d1899e7ff33cd515b0eb](https://github.com/MarlinFirmware/Marlin/commit/373f3ecab3ea9cb18d83d1899e7ff33cd515b0eb)
- First parent (base): [e36d31a3b7b699324d38d4b6d60d9e8ec638c114](https://github.com/MarlinFirmware/Marlin/commit/e36d31a3b7b699324d38d4b6d60d9e8ec638c114)
- Second parent (remote): [9e7b5056a0a02921d1e31d511b34efc9732e3c88](https://github.com/MarlinFirmware/Marlin/commit/9e7b5056a0a02921d1e31d511b34efc9732e3c88)

## Task
Merge _base_ with _remote_.
This task contains one file to merge: `Marlin_main.cpp`.

The functionality for movement is different in the `remote` than in the `base`, therefore these `remote` changes should be part of a `DELTA` feature.

The `base` evolutions should in general be accepted. There are significant whitespace differences.

* In `case 28:`, accept the `remote` changes adding `current_position[n] = destination[n]`.
* In `case 28:`, the differences for `plan_set_position` between `base` and `remote` should be part of a `DELTA` feature.
* In `prepareMove()`, the differences between `base` and `remote` should be part of a `DELTA` feature.
