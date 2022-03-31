import click
import json
from os import chdir
from os.path import exists, dirname, realpath
from subprocess import getstatusoutput, run


path = dirname(dirname(realpath(__file__)))


@click.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--event", default="on-change", help="Event")
@click.option("--script", default="run", help="The script to run when the event occurs")
def cli(file, event, script):
    """This is description"""
    checkParams(event, script)
    updateJson(realpath(file), event, script)
    watch(event, script)


def checkParams(event, script):
    if exists(path + "/events/" + event) == False:
        raise click.UsageError(
            f"Invalid value for '--event': Path 'events/{event}' does not exist."
        )
    if exists(path + "/scripts/" + script) == False:
        raise click.UsageError(
            f"Invalid value for '--script': Path 'scripts/{script}' does not exist."
        )


def updateJson(b, u, g):
    with open(path + "/data/oderint.json", "r+") as config:
        data = json.load(config)

        data["file"] = b
        data["event"] = u
        data["script"] = g

        config.seek(0)
        json.dump(data, config, indent=4)
        config.truncate()


def watch(event, script):
    chdir(path)

    while True:
        status, output = getstatusoutput(path + "/events/" + event)

        if status == 0:
            run(path + "/scripts/" + script)
        else:
            raise click.ClickException(output)


if __name__ == "__main__":
    cli()