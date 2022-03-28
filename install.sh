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
}

uninstall () {
    rm -r $path
}

if [ $# -eq 0 ]; then
	install
elif [ $1 == "-r" ]; then
	uninstall
fi
