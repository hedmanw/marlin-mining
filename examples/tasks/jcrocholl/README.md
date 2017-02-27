# jcrocholl
- Merging fork [jcrocholl/Marlin#c295a14b2822bf3882730fd5816628221187c287](https://github.com/jcrocholl/Marlin/commit/c295a14b2822bf3882730fd5816628221187c287)
- into mainline [MarlinFirmware/Marlin#5f555140be4231fb3ffea8a407414e245cfc12ec](https://github.com/MarlinFirmware/Marlin/commit/5f555140be4231fb3ffea8a407414e245cfc12ec)

## Task
The task is to merge the `fork` files into the `mainline` files.
The task contains one file to merge: `Marlin_main_cleaned.cpp`.
The general rule is to accept `fork` changes as evolution, and to accept `mainline` changes that are not in the `fork`.

## Results
Numbers indicate the line numbers of the MPS result, when diffed with the Eclipse result.
Cross-referenced with parents and task description to derive what went wrong.

* _Integration_ Lost else-branch in integration: 1024
* _Integration_ Lost DELTA feature wrapping: 1078
* _Tool_ Block moved out of else-branch before if: 1053, 1516


### Sums
* Integration: 2
* Tool: 1 + 1 (elif)