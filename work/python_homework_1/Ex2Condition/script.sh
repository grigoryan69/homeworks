#!/usr/bin/bash

python Ex2-Condition.py < test1.txt > output1.txt
python Ex2-Condition.py < test2.txt > output2.txt
python Ex2-Condition.py < test3.txt > output3.txt

output1=`cat output1.txt`
output2=`cat output2.txt`
output3=`cat output3.txt`

if [[ $output1 == "Your number ?: 1" ]] && [[ $output2 == "Your number ?: 2" ]] && [[ $output3 == "Your number ?: 0" ]]
then
   echo 'test passed successfully'
else
   echo 'test failed successfully'
fi