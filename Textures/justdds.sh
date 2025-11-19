#!/bin/bash

# Convert all png to dss

export WINEDEBUG=-all
find . -type f -iname "*.png" -print0 | while read -d $'\0' file
do
    checkfileroot=${file::-4}
    echo "Going to process $file..."
    cp $file temp.png
    wine texconv.exe -y -m 1 -f BC7_UNORM -nologo temp.png
    rm -f $checkfileroot.DDS
    rm -f $checkfileroot.dds
    mv temp.dds $checkfileroot.dds
    rm temp.png
done
