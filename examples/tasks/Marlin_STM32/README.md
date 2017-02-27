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
* _Integration_ Illegal syntax, incorrectly integrated: 403
* _Integration_ Incorrectly integrated, missing block: 589
* _Tech_ * Else/elif-branch appears partially: 1421

`planner.cpp`
_No diffs._

`stepper.cpp`
* _Integration_ Fork artifact still present: 138, 239, 380, 399, 412, 438, 640, 828, 848, 866, 1087
* _Diff_ Feature AT90USB missing: 638
* _Tech_ If-block moved: 339
* _Tech_ Block from inside if moved out above it: 656
* _Tech_ Block moved below where it should be: 1104
