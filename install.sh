#!/bin/bash

app="oderint"
path="$HOME/.$app"
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
}

uninstall () {
    rm -r $path
}

if [ $# -eq 0 ]; then
	install
elif [ $1 == "-r" ]; then
	uninstall
fi
