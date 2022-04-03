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

removeText () {
    wordCount=$(grep -o "$(cat $textFile)" $destFile | wc -l)
    isTextExists=$([[ $wordCount -ne 0 ]] && echo true || echo false)

    if $isTextExists; then
        diff $destFile $textFile | sed -n 's/^< //p' > $tempFile
        lineCount=$(cat $tempFile | wc -l)
        echo "$(head -$lineCount $tempFile)" > $destFile
        rm $tempFile
    fi
}
