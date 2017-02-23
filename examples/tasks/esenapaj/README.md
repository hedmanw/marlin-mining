# esenapaj
- Merging fork [esenapaj/Marlin#a1b8475b9377193b908fe4d08b6f44f14c363971](https://github.com/esenapaj/Marlin/commit/a1b8475b9377193b908fe4d08b6f44f14c363971)
- into mainline [MarlinFirmware/Marlin#34d5eb5201f4960c9427e33e0805c0063f657203](https://github.com/MarlinFirmware/Marlin/commit/34d5eb5201f4960c9427e33e0805c0063f657203)


## Task
The task is to merge the `fork` files into the `mainline` files. The general rule is to accept `fork` changes as evolution.
Some parts of `fork` changes should however be considered as features, and should be handled as given below:

For `Marlin_main.cpp`:
* Any added changes under the presence condition `defined(ADDITIONAL_EXPERIMENTAL_FEATURES) && MB(ALLIGATOR)` should be integrated under the feature `ESENPAJ`.
* There are a nubmer of changes where a function name is in lowercase in the `mainline` and in uppercase in the `fork` (ex: `floor` -> `FLOOR`). These changes should be integrated under the feature `ESENPAJ`, and `NOT ESENPAJ`, respectively.

