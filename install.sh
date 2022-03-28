#!/bin/bash

app="oderint"
path="$HOME/.$app"
dirs=("data" "events" "scripts" "src")
files=("setup.py")

if [ $# -eq 0 ]; then
	install
elif [ $1 == "-r" ]; then
	uninstall
fi
