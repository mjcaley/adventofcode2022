from io import StringIO
from pathlib import Path

import typer

from .calorie_parser import parse, top1, top3


def cli1(data: Path):
    with open(data) as file:
        lines = file.readlines()

    result = top1(parse(lines))
    typer.echo(result)


def cli2(data: Path):
    with open(data) as file:
        lines = file.readlines()

    result = top3(parse(lines))
    typer.echo(result)


def run1():
    typer.run(cli1)


def run2():
    typer.run(cli2)
