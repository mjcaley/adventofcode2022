from pathlib import Path
import typer
from .packet import parse2


def cli(data: Path):
    with open(data) as file:
        line = file.read()

    typer.echo(parse2(line))


def run():
    typer.run(cli)