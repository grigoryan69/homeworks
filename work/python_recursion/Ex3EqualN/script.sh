#!/usr/bin/bash
input=`cat input.txt`
output=`cat output.txt`

if [[ $input == 123 ]] && [[ $output == 7021 ]]
then
   echo 'test passed successfully'
else
   echo 'test failed successfully'
fi