#!/usr/bin/env bash

printf $1
printf " "
git show --pretty=%P $1 | head -1