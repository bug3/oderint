import json
from os.path import dirname, basename, splitext

f = open("data/oderint.json")
config = json.load(f)
f.close()
