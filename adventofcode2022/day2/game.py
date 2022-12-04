from enum import IntEnum
from typing import Generator


class Shape(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3


class Outcome(IntEnum):
    Loss = 0
    Draw = 3
    Win = 6


def parse_move(move: str) -> Shape:
    return {
        "A": Shape.Rock,
        "B": Shape.Paper,
        "C": Shape.Scissors,
        "X": Shape.Rock,
        "Y": Shape.Paper,
        "Z": Shape.Scissors
    }[move]


def parse_outcome(outcome: str) -> Outcome:
    return {
        "X": Outcome.Loss,
        "Y": Outcome.Draw,
        "Z": Outcome.Win
    }[outcome]


def parse_round(line: str):
    opponent = parse_move(line[0])
    player = parse_move(line[2])

    return (opponent, player)


def calculate_outcome(opponent: Shape, player: Shape) -> Outcome:
    if opponent == player:
        return Outcome.Draw
    
    if opponent is Shape.Rock and player is Shape.Scissors:
        return Outcome.Loss
    elif opponent is Shape.Scissors and player is Shape.Paper:
        return Outcome.Loss
    elif opponent is Shape.Paper and player is Shape.Rock:
        return Outcome.Loss

    if player is Shape.Rock and opponent is Shape.Scissors:
        return Outcome.Win
    elif player is Shape.Scissors and opponent is Shape.Paper:
        return Outcome.Win
    elif player is Shape.Paper and opponent is Shape.Rock:
        return Outcome.Win



def calculate_round_score(round: tuple[Shape, Shape]) -> int:
    outcome = calculate_outcome(round[0], round[1])

    return round[1] + outcome


def calculate_game_score(rounds: list[tuple[Shape, Shape]]) -> int:
    return sum(map(calculate_round_score, rounds))


def parse(lines: list[str]) -> int:
    rounds = []
    
    for line in lines:
        opponent = parse_move(line[0])
        player = parse_move(line[2])

        rounds.append((opponent, player))

    return calculate_game_score(rounds)


def calculate_move(opponent: Shape, outcome: Outcome) -> Shape:
    if outcome is Outcome.Draw:
        return opponent
    elif outcome is Outcome.Loss:
        loss = {
            Shape.Rock: Shape.Scissors,
            Shape.Paper: Shape.Rock,
            Shape.Scissors: Shape.Paper
        }
        return loss[opponent]
    elif outcome is Outcome.Win:
        win = {
            Shape.Rock: Shape.Paper,
            Shape.Paper: Shape.Scissors,
            Shape.Scissors: Shape.Rock
        }
        return win[opponent]


def parse2(lines: list[str]) -> int:
    rounds = []

    for line in lines:
        opponent = parse_move(line[0])
        outcome = parse_outcome(line[2])
        player = calculate_move(opponent, outcome)

        rounds.append((opponent, player))

    return calculate_game_score(rounds)
