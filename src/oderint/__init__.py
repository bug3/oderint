import click
import json
from os import chdir, system
from os.path import exists, dirname, realpath, isdir
from subprocess import getstatusoutput, run


config = {}
info = {}


@click.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("--event", help="Event to be listen")
@click.option("--script", help="The script to run when the event occurs")
@click.option("--run-first", help="Run script without listening for event")
@click.option("--port", help="Shows which port to open localhost")
def cli(path, event, script, run_first, port):
    """This is description"""
    global config, info

    config["path"] = realpath(path)
    config["event"] = event
    config["script"] = script if script is None else script.split(" ")
    config["run-first"] = run_first
    config["port"] = port

    info["isDir"] = isdir(path)

    chdir(dirname(dirname(dirname(realpath(__file__)))))
    updateJson()
    checkParams()
    watch()


def checkParams():
    if exists("events/" + config["event"]) == False:
        raise click.UsageError(
            f"Invalid value for '--event': Path 'events/{config['event']}' does not exist."
        )

    for i in config["script"]:
        if exists("scripts/" + i) == False:
            raise click.UsageError(
                f"Invalid value for '--script': Path 'scripts/{i}' does not exist."
            )


def updateJson():
    with open("data/oderint.json", "r+") as configFile:
        data = json.load(configFile)

        for i in config:
            if config[i] != None:
                data[i] = config[i]
            else:
                config[i] = data[i]

        configFile.seek(0)
        json.dump(data, configFile, indent=4)
        configFile.truncate()


def watch():
    if config["run-first"]:
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

    for i in config["script"]:
        run("scripts/" + i)


if __name__ == "__main__":
    cli()
