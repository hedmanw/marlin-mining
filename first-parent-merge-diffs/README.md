# Merge diffs
The subdirectory `Marlin_main` contains the entire merge history of `Marlin_main.cpp`, generated using

    $ git log -U -m --simplify-merges --merges --first-parent -- Marlin/Marlin_main.cpp

This is then split into one diff per file.

This directory follows only the first merge parent. What this means is that the changes of the integrated branch is "squashed" into a single diff, meaning that unique commits in the fork is lost, but the entire changeset is kept.