#!/usr/bin/bash

python Ex4-triangle.py < inputs.txt > output.txt 

output=`cat output.txt`

if [[ $output == "Enter length of 1 Figure: Enter length of 2 Figure: Area of the triangle: 50.0" ]]
then
   echo 'test passed successfully'
else
   echo 'test failed successfully'
fi