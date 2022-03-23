#!/usr/bin/bash
input=`cat input.txt`
output=`cat output.txt`

if [[ $input == 5 ]] && [[ $output == '0, 1, 1, 2, 3' ]]
then
   echo 'test passed successfully'
else
   echo 'test failed successfully'
fi