#!/usr/bin/env bash

grep $1* -l -E -e "(\+|-)\s*#(.*if((n?)def| (not )?defined)|else)"
