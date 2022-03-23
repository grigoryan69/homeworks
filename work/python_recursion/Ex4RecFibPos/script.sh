#!/usr/bin/bash
input=`cat input.txt`
output=`cat output.txt`

if [[ $input == 7 ]] && [[ $output == 8 ]]
then
   echo 'test passed successfully'
else
   echo 'test failed successfully'
fi