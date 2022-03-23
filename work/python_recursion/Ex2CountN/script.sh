#!/usr/bin/bash
input=`cat input.txt`
output=`cat output.txt`

if [[ $input == 333 ]] && [[ $output == 55611 ]]
then
   echo 'test passed successfully'
else
   echo 'test failed successfully'
fi