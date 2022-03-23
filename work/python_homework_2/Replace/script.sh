#!/usr/bin/bash

output=`cat output.txt`
input=`cat input.txt`

if [[ $output == $input ]]
then
   echo 'test passed successfully'
else
   echo 'test failed successfully'
fi