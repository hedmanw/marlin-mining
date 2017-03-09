#!/usr/bin/env bash

find . -type f -name "*.cpp" | xargs -0 ./aux.sh
find . -type f -name "*.h" | xargs -0 ./aux.sh