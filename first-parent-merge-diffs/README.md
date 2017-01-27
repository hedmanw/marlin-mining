# Merge diffs
The subdirectory `Marlin_main` contains the entire merge history of `Marlin_main.cpp`, generated using

    $ git log -U -m --simplify-merges --merges --first-parent -- Marlin/Marlin_main.cpp

This is then split into one diff per file.

This directory follows only the first merge parent. This is complicated by the fact that merges that took place in a
fork are also included in the tree of the mainline, since it is also merged in the pull request.

It seems though that this is not a problem, since in an approved pull request, the requestee will be the first parent.