#!/usr/bin/bash
input=`cat input.txt`
output=`cat output.txt`

if [[ $input == 5 ]] && [[ $output == 120 ]]
then
   echo 'test passed successfully'
else
   echo 'test failed successfully'
fi