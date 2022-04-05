#!/bin/bash

path=$(jq -r ".path" data/oderint.json)
event=$(jq -r ".event" data/oderint.json)
script=$(jq -r ".script" data/oderint.json)
port=$(jq -r ".port" data/oderint.json)

dirname=$(dirname $path)
tempFile="temp.out"

fileName=${path##*/}
fileExt=${path##*.}
