#!/bin/bash
# Convert a text string to letter-at-a-time formatted .ass snippet
#echo "hello!"
#echo $1
string=$1
cc=0
finaloutput="{\fad(0,133)}"
for ((k=0;k<${#string};++k)); do
    #echo "Character $k is '${string:k:1}'"
    low=$(((($cc*2000)+15)/30))
    high=$((((($cc*2)+4)*1000)/30))
    #echo $low
    #echo $high
    #((++cc))
    if [[ ${string:k:1} == " " ]]; then
        #echo "SPACE!"
        :
    else
        #echo "no space"
        ((++cc))
        finaloutput="$finaloutput{\alpha&HFF&}{\t($low,$high,0.5,\alpha&H00&)}"
    fi
    finaloutput="$finaloutput${string:k:1}"
done
echo $finaloutput
