# Marlin_STM32
- Merging fork [MakerLabMe/Marlin_STM32#cb1373b696407cf7d74e0c5ff2c91a8539b085a6](https://github.com/MakerLabMe/Marlin_STM32/commit/cb1373b696407cf7d74e0c5ff2c91a8539b085a6)
- into mainline [MarlinFirmware/Marlin#45336bb6c041c90ada2da533d3f6ead8f4bd0031](https://github.com/MarlinFirmware/Marlin/commit/45336bb6c041c90ada2da533d3f6ead8f4bd0031)

## Task
The task is to merge the `fork` files into the `mainline` files.
The task contains three files to merge: `Marlin_main_cleaned.cpp`, `planner_cleaned.cpp`, `stepper_cleaned.cpp`.
The files have been stripped from whitespaces at the end of lines, in order to not cause unintentional differences.

Changes from the `fork` should in general be accepted as evolution, in particular, the `fork` replaces the type `int` with `int16_t`. These changes should always be accepted.

For all files:
* The `fork` adds debug printing lines with `Serial.println()`. These should always be discarded.

For `Marlin_main_cleaned.cpp` only:
* Additions in the `fork` should be integrated under the feature `ARDUINO_ARCH_STM32`.
