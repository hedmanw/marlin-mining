# Merge diffs
The subdirectory `Marlin_main` contains the entire merge history of `Marlin_main.cpp`, generated using

    $ git log -U -m --simplify-merges --merges -- Marlin/Marlin_main.cpp

This is then split into one diff per file.
