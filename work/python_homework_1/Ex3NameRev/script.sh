#!/usr/bin/bash
python Ex3_name_rev.py < input.txt > output.txt

output=`cat output.txt`

if [[ $output == 'Enter your name: emanrasu eman' ]]
then
    echo 'test passed successfully'
else
    echo 'test failed successfully'
fi