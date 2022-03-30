#!/bin/bash

app="oderint"
path="$HOME/.$app"
localPath="$HOME/.local"
dirs=("data" "events" "scripts" "src")
files=("setup.py")

install () {
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

    cd $path
    pip install -e .
}

uninstall () {
    rm -r $path
    rm $localPath/bin/oderint
}

if [ $# -eq 0 ]; then
	install
elif [ $1 == "-r" ]; then
	uninstall
fi
