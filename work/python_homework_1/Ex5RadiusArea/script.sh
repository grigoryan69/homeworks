#!/usr/bin/bash

python Ex5-radius-area.py > output.txt

output1=`cat output.txt`
output2=`cat real_output.txt`

if [[ $output1 == $output2 ]]
then
   echo 'test passed successfully'
else
   echo 'test failed successfully'
fi