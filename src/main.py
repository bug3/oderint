import click
import json
from os.path import dirname, realpath
from subprocess import getstatusoutput, run


@click.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--event", default="on-change", help="Event")
@click.option("--script", default="run", help="The script to run when the event occurs")
def cli(event, script):
    """This is description"""
    click.echo(f"event={event} script={script}")


def test():
    path = dirname(dirname(realpath(__file__)))
    status, output = getstatusoutput(path + "/events/on-change")

    if status == 0:
        run(path + "/scripts/run")
    else:
        print(output)


if __name__ == "__main__":
    test()
