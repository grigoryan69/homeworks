#!/usr/bin/bash

output=`cat output.txt`

if [[ $output ]]
then
   echo 'test passed successfully'
else
   echo 'test failed successfully'
fi