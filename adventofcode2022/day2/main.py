from pathlib import Path
import typer
from .game import parse


def cli1(data: Path):
    with open(data) as file:
        lines = file.readlines()

    typer.echo(parse(lines))


def run1():
    typer.run(cli1)