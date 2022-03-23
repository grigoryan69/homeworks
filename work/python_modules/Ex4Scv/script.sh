#!/usr/bin/bash
real_output=`cat true_data.csv`
true_output=`cat data.csv`

if [[ $true_output == $real_output ]]
then
   echo 'test passed successfully'
else
   echo 'test failed successfully'
fi