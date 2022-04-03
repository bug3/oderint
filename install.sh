#!/bin/bash

app="oderint"
path="$HOME/.$app"
localPath="$HOME/.local"
dirs=("data" "events" "scripts" "src")
files=("setup.py")

install() {
    if [[ ! -e $path ]]; then
        mkdir $path
    else
        echo "$path already exists"
        exit 1
    fi

    for dir in ${dirs[@]}; do
        cp -r $dir $path
    done

    for file in ${files[@]}; do
        cp $file $path
    done

    appendText

    cd $path
    pip install -e .
}

uninstall() {
    removeText

    rm -r $path
    rm $localPath/bin/oderint
}

source data/append-remove.sh $HOME/.vimrc data/vimrc

if [ $# -eq 0 ]; then
    install
elif [ $1 == "-r" ]; then
    uninstall
fi
