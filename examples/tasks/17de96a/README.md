# 17de96a
- Result commit: [17de96ace7c02631fc047dcddd817a59c965e849](https://github.com/MarlinFirmware/Marlin/commit/17de96ace7c02631fc047dcddd817a59c965e849)
- First parent (base): [ab355a90d33ed457d964fe97f675f79720863585](https://github.com/MarlinFirmware/Marlin/commit/ab355a90d33ed457d964fe97f675f79720863585)
- Second parent (remote): [7458bfe297d6f8ebe528b31b60c838a484e74e84](https://github.com/MarlinFirmware/Marlin/commit/7458bfe297d6f8ebe528b31b60c838a484e74e84)

## Task
Merge _base_ with _remote_.
This task contains one file to merge: `cardreader.cpp`.

In general, the remote changes should be discarded, in particular, discard every block related to the `SDCARD_SORT_ALPHA` feature.
This means that in general, the base changes should be accepted. The exceptions to this are listed below:
* Accept the `LCD_SDSS` feature changes from `remote`
* Accept `getfilename()` call(s) from `remote`
* Accept `CardReader::getfilename` function signature from `remote` and changes to `lsDive()` inside the function.