#!/usr/bin/bash
counter=`cat counter.txt`
elements=`cat elements.txt`

if [[ $elements == '1, 2, 3, 4' ]]
then
   echo 'test passed successfully'
else
   echo 'test failed successfully'
fi