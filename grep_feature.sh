#!/usr/bin/env bash

grep * -E -e "(\+|-)\s*#.*if((n?)def $1| (not )?defined\($1)"
