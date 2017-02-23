# 3116271
- Result commit: [311627141bff077a4c5ac6e602fcf6d1c7ae22ca](https://github.com/MarlinFirmware/Marlin/commit/311627141bff077a4c5ac6e602fcf6d1c7ae22ca)
- First parent (base): [85da81e67349ab815985b5651aecfb7943201b3c](https://github.com/MarlinFirmware/Marlin/commit/85da81e67349ab815985b5651aecfb7943201b3c)
- Second parent (remote): [2d9a7156555e0cdd969b44cc7c4d3c8a18875cfe](https://github.com/MarlinFirmware/Marlin/commit/2d9a7156555e0cdd969b44cc7c4d3c8a18875cfe)

## Task
Merge _base_ with _remote_.
This task contains one file to merge: `temperature.h`.

In general, the remote should be integrated as evolution. There are some exceptions to this.
The following declarations should be kept as is in `temperature.h`, and the remote changes to them discarded.
* `inline float degTargetBed`
* `inline void setTargetBed`
* `inline bool isHeatingBed`
* `inline bool isCoolingBed`
