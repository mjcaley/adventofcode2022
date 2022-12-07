from pathlib import Path
import typer
from .disk import parse1


def cli(data: Path):
    with open(data) as file:
        lines = file.readlines()

    typer.echo(parse1(lines))


def run():
    typer.run(cli)
