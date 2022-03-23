#!/usr/bin/bash

output1=`cat intTester.txt`
output2=`cat strTester.txt`

if [[ $output1 == 'This is number' ]] && [[ $output2 == 'This is not number' ]]
then
   echo 'test passed successfully'
else
   echo 'test failed successfully'
fi