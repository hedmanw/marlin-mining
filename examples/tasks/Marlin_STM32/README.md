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

## Results
Numbers indicate the line numbers of the MPS result, when diffed with the Eclipse result.
Cross-referenced with parents and task description to derive what went wrong.

`Marlin_main.cpp`
* _Integration_ Fork artifact still present: 575, 584
* _Diff_ Missing wrapping in ARDUINO_ARCH_STM32 feature: 1448
* _Tech_ Block missing: 1513

`planner.cpp`
_No diffs._

`stepper.cpp`
* _Integration_ Fork artifact still present: 476
* _Integration_ Presence condition ARDUINO_ARCH_STM32 missing: 160, 202, 243, 277, 613, 646, 664, 679
* _Integration_ Feature ARDUINO_ARCH_STM32 wrapped in ARDUINO_ARCH_STM32: 893
* _Tech_ Blocks missing: 557, 572, 582
* _Tech_ Block moved: 935, 1190

### Sums

* Integration: 2 + 10
* Diff: 1
* Tech: 1 + 1 + 1 (elif)