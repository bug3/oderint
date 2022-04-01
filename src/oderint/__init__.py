import click
import json
from os import chdir, system
from os.path import exists, dirname, realpath, isdir
from subprocess import getstatusoutput, run


config = {}
info = {}


@click.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("--event", default="on-change", help="Event to be listen")
@click.option("--script", default="run", help="The script to run when the event occurs")
@click.option("--runfirst", default=True, help="Run script without listening for event")
@click.option("--port", default=3000, help="Shows which port to open localhost")
def cli(path, event, script, runfirst, port):
    """This is description"""
    global config, info

    config["path"] = realpath(path)
    config["event"] = event
    config["script"] = script
    config["runFirst"] = runfirst
    config["port"] = port

    info["isDir"] = isdir(path)

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
    if config["runFirst"]:
        runScript()

    try:
        listenEvent()
    except KeyboardInterrupt:
        if info["isDir"]:
            run("scripts/close-port")


def listenEvent():
    while True:
        status, output = getstatusoutput("events/" + config["event"])

        if status == 0:
            runScript()
        else:
            raise click.ClickException(output)


def runScript():
    if not info["isDir"]:
        system("clear")

    run("scripts/" + config["script"])


if __name__ == "__main__":
    cli()
