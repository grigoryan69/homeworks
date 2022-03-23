#!/usr/bin/bash
python Ex8-multi-taple.py < input.txt > output.txt

input=`cat input.txt`
output=`cat output.txt`

while read -r line;
do
   echo "$line" > output.txt;
done < output.txt 
output=`cat output.txt`

if [[ $input == 5 ]] && [[ $output == 'enter your number:5 * 1 = 5' ]]
then
   echo 'test passed successfully'
else
   echo 'test failed successfully'
fi