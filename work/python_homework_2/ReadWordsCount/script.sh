#!/usr/bin/bash

output=`cat output.txt`
input=`cat input.txt`

if [[ $output == 1 ]] && [[ $input == 'long' ]]
then
   echo 'test passed successfully'
else
   echo 'test failed successfully'
fi