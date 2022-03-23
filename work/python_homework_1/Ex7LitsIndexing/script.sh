#!/usr/bin/bash
python Ex7-listindex.py > real_output.txt

real_output=`cat real_output.txt`
true_output=`cat true_output.txt`

if [[ " ${true_output[*]} " == " ${real_output[*]} " ]]
then
   echo 'test passed successfully'
else
   echo 'test failed successfully'
fi
