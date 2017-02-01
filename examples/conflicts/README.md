## Structure and conventions
Each subdirectory contains a `README.txt`, with links to the involved commits for traceability.
Directories:
- `merge_excerpts`: Contains conflict excerpts of the working tree _during_ the merge.
- `whole_files`: Contains copies of the involved files in the working tree at four points:
    1. First parent (prefix `base`)
    2. Second parent (prefix `remote`)
    3. Snapshot of working tree _during_ the merge (prefix `merge`)
    4. Merge commit or "outcome" (prefix `result`)