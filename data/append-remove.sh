#!/bin/bash

destFile=$1
textFile=$2
tempFile=.vimrc-oderint.tmp

cp $destFile $destFile.bak

appendText () {
    wordCount=$([[ -f $destFile ]] && cat $destFile | wc -w)

    ed -s $destFile <<< w
    
    if [[ $wordCount -eq 0 ]]; then
        tail -n +2 $textFile > $destFile
    else
        cat $textFile >> $destFile
    fi    
}
