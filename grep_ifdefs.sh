#!/usr/bin/env bash

mergedir=$1"*"
grep $mergedir -n -E -e "(\+|-)\s*#((el)?if((n?)def| ((not )?defined)|(EN|DIS)ABLED)|else)"

# grep * -n -E -e "(\+|-)\s*#((el)?if((n?)def| ((not )?defined)|(EN|DIS)ABLED)|else)" #140336
# grep * -n -E -e "(\+|-)\s*#((el)?if((n?)def| ((not )?defined)|(EN|DIS)ABLED))" #110833