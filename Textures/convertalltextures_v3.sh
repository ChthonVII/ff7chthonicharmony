#!/bin/bash

# Use this to apply reverse-color-correction such that
# the output file displayed in NTSC-J mode looks the same as
# the input file displayed in sRGB mode.

export WINEDEBUG=-all
find . -type f -iname "*.dds" -print0 | while read -d $'\0' file
do
    #echo $file
    checkfileroot=${file::-4}
    #echo $checkfileroot
    checkfileA="$checkfileroot.png"
    #echo $checkfileA
    checkfileB="$checkfileroot.PNG"
    #echo $checkfileB
    if test -f "$checkfileA"; then
        echo "$checkfileA exists; so skipping $file."
    else
        if test -f "$checkfileB"; then
            echo "$checkfileB exists; so skipping $file."
        else
            echo "Going to process $file..."
            cp $file temp.dds
            wine texconv.exe -ft png temp.dds
            #./ntscjpng srgb-to-ntscj temp.png temp-out.png
            ./gamutthingy --crtemu front --crtdemod CXA2060BS_JP --crtyuvconst 3digit --crtclamphighenable false --crtclamplowzerolight true --crtblack 0.0018 --crtwhite 1.5 --crt-saturation-knob 1.04 --source-primaries P22_trinitron_mixandmatch --source-whitepoint 9300K8mpcd --dest-primaries srgb_spec --dest-whitepoint D65 --adapt cat16 --spiral-carisma true --map-mode compress --gamut-mapping-algorithm vprc --gamma-out srgb --backwards true --infile temp.png --dither false --outfile temp-out.png
            wine texconv.exe -y -m 1 -f BC7_UNORM -nologo temp-out.png
            mv temp-out.dds $file
            rm temp.png
            rm temp-out.png
            rm temp.dds
        fi
    fi
done
find . -type f -iname "*.png" -print0 | while read -d $'\0' file
do
    checkfileroot=${file::-4}
    echo "Going to process $file..."
    cp $file temp.png
    #./ntscjpng srgb-to-ntscj temp.png temp-out.png
    ./gamutthingy --crtemu front --crtdemod CXA2060BS_JP --crtyuvconst 3digit --crtclamphighenable false --crtclamplowzerolight true --crtblack 0.0018 --crtwhite 1.5 --crt-saturation-knob 1.04 --source-primaries P22_trinitron_mixandmatch --source-whitepoint 9300K8mpcd --dest-primaries srgb_spec --dest-whitepoint D65 --adapt cat16 --spiral-carisma true --map-mode compress --gamut-mapping-algorithm vprc --gamma-out srgb --backwards true --infile temp.png --dither false --outfile temp-out.png
    wine texconv.exe -y -m 1 -f BC7_UNORM -nologo temp-out.png
    mv temp-out.png $file
    rm -f $checkfileroot.DDS
    rm -f $checkfileroot.dds
    mv temp-out.dds $checkfileroot.dds
    rm temp.png
done
