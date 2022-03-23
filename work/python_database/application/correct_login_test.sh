#!/usr/bin/bash
python database.py < input.txt > real_output.txt
Check=$(diff golden_output.txt real_output.txt)

if [[ $Check == "" ]]
then
    echo 'login working correct pass'
else
    echo 'collapse'
fi


