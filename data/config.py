import json
from os.path import dirname, basename, splitext

f = open("data/oderint.json")
config = json.load(f)
f.close()

path = config["path"]
event = config["event"]
script = config["script"]
port = config["port"]

tempFile = "temp.out"
dirName = dirname(path)
fileName = basename(path)
fileExt = splitext(path)
