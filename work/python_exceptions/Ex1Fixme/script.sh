#!/usr/bin/bash
output=`cat output.txt`

if [[ $output == '0 != 6' ]]
then
   echo 'test passed successfully'
else
   echo 'test failed successfully'
fi