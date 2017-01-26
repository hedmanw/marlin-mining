# Merge diffs
The subdirectory `Marlin_main` contains the entire merge history of `Marlin_main.cpp`, generated using

    $ git log -U -m --simplify-merges --merges -- Marlin/Marlin_main.cpp

This is then split into one diff per file.
I will investigate more into what changes if `--first-parent` is supplied too. This comes from the complicating fact
that merges that took place in a fork are also included in the tree of the mainline, since it is also merged in the
pull request.
