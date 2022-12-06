from pathlib import Path
import typer
from .packet import parse1


def cli(data: Path):
    with open(data) as file:
        line = file.read()

    typer.echo(parse1(line))


def run():
    typer.run(cli)
