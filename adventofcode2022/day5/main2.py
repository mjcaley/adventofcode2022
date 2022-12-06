from pathlib import Path
import typer
from .stacks import parse2


def cli(data: Path):
    with open(data) as file:
        lines = file.readlines()

    typer.echo(parse2(lines))


def run():
    typer.run(cli)