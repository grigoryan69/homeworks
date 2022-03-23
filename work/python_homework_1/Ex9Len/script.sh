#!/usr/bin/bash

python Ex9-num-leng.py < input.txt > output.txt

input=`cat input.txt`
output=`cat output.txt`

if [[ $input == 10 ]] && [[ $output == 'enter some number: The length - 2' ]]
then
   echo 'test passed successfully'
else
   echo 'test failed successfully'
fi