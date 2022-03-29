import click
import json
from os.path import exists, dirname, realpath
from subprocess import getstatusoutput, run


@click.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--event", default="on-change", help="Event")
@click.option("--script", default="run", help="The script to run when the event occurs")
def cli(file, event, script):
    """This is description"""
    checkParams(event, script)


def checkParams(event, script):
    if exists("events/" + event) == False:
        raise click.UsageError(
            f"Invalid value for '--event': Path 'events/{event}' does not exist."
        )
    if exists("scripts/" + script) == False:
        raise click.UsageError(
            f"Invalid value for '--script': Path 'scripts/{script}' does not exist."
        )


if __name__ == "__main__":
    cli()
