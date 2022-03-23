#!/usr/bin/bash
python Ex6-circle_radius.py < input.txt > output.txt

output1=`cat output.txt`
if [[ $output1 == 'Input the radius of the circle : The area of the GoCircle with radius 10.0 is: 314.1592653589793' ]]
then
   echo 'test passed successfully'
else
   echo 'test failed successfully'
fi