#!/usr/bin/bash

coverage run unit.py
coverage html unit.py
coverage report -m

UNAME=$(uname)

if [ "$UNAME" == "Linux" ] ; then
	echo "Linux detected"
    cd htmlcov 
    open index.html
    open unit_py.html
    cd ../

elif [[ "$UNAME" == CYGWIN* || "$UNAME" == MINGW* ]] ; then
	echo "Windows detected"
    cd htmlcov 
    start index.html
    start unit_py.html
    cd ../

fi