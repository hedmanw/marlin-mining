# 47c1ea7
- Result commit: [47c1ea72aff276a9ea0317aba8b400a49ac9e7dc](https://github.com/MarlinFirmware/Marlin/commit/47c1ea72aff276a9ea0317aba8b400a49ac9e7dc)
- First parent (base): [e650d4044ede9b8e44bf84e9bea6b257b0503d8d](https://github.com/MarlinFirmware/Marlin/commit/e650d4044ede9b8e44bf84e9bea6b257b0503d8d)
- Second parent (remote): [8ccdac9898ca1c724e076ce1de6e4fd2fe4ad622](https://github.com/MarlinFirmware/Marlin/commit/8ccdac9898ca1c724e076ce1de6e4fd2fe4ad622)

## Task
Merge _base_ with _remote_.
This task contains one file to merge: `temperature.cpp`.

In general, accept all the `base` changes, discard all the `remote` changes.
Except for the `remote` change `PID_DEBUG` feature, which should be integrated into the bottom of the `get_pid_output_bed()` function.