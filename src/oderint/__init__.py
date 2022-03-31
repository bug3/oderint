import click
import json
from os import chdir, system
from os.path import exists, dirname, realpath, splitext
from subprocess import getstatusoutput, run


config = {}
info = {}


@click.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--event", default="on-change", help="Event to be listen")
@click.option("--script", default="run", help="The script to run when the event occurs")
@click.option("--runfirst", default=True, help="Run script without listening for event")
@click.option("--port", default=3000, help="Shows which port to open localhost")
def cli(file, event, script, runfirst, port):
    """This is description"""
    global config, info

    config["file"] = realpath(file)
    config["event"] = event
    config["script"] = script
    config["runFirst"] = runfirst
    config["port"] = port

    info["extension"] = splitext(file)[1]

    chdir(dirname(dirname(dirname(realpath(__file__)))))
    checkParams()
    updateJson()
    watch()


def checkParams():
    if exists("events/" + config["event"]) == False:
        raise click.UsageError(
            f"Invalid value for '--event': Path 'events/{config['event']}' does not exist."
        )
    if exists("scripts/" + config["script"]) == False:
        raise click.UsageError(
            f"Invalid value for '--script': Path 'scripts/{config['script']}' does not exist."
        )


def updateJson():
    with open("data/oderint.json", "r+") as configFile:
        data = json.load(configFile)

        for i in config:
            data[i] = config[i]

        configFile.seek(0)
        json.dump(data, configFile, indent=4)
        configFile.truncate()


def watch():
    while True:
        status, output = getstatusoutput("events/" + config["event"])

        if status == 0:
            runScript()
        else:
            raise click.ClickException(output)


def runScript():
    if info["extension"] != ".html":
        system("clear")

    run("scripts/" + config["script"])


if __name__ == "__main__":
    cli()
