#!/usr/bin/bash

output=`cat output.txt`

if [[ $output == 7 ]]
then
   echo 'test passed successfully'
else
   echo 'test failed successfully'
fi