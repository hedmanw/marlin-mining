#!/usr/bin/env bash

mergedir=$1"merge_excerpts/*"
grep $mergedir -n -E -e "#.*if((n?)def| (not )?defined)"