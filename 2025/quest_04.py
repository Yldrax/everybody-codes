"""Fourth Day"""

from math import floor, ceil
from utils import load_input


def calc_ratio(gears: list[int]) -> float:
    ratio = 1.0
    for i in range(len(gears) - 1):
        ratio *= gears[i] / gears[i + 1]
    return ratio


def calc_coupled_ratio(gears: list[list[int]]) -> float:
    ratio = 1.0
    for i in range(len(gears) - 1):
        g1 = gears[i][0] if len(gears[i]) == 1 else gears[i][1]
        g2 = gears[i + 1][0]
        ratio *= g1 / g2

    return ratio


def calc_turns(gears: list[int]) -> int:
    return floor(calc_ratio(gears) * 2025)


def calc_min_turns(gears: list[int]) -> int:
    return ceil(10000000000000 / calc_ratio(gears))


def calc_turns_coupled(gears: list[list[int]]) -> int:
    return floor(calc_coupled_ratio(gears) * 100)


if __name__ == "__main__":
    INPUT1 = load_input(2025, 4, 1)
    INPUT1 = [int(n) for n in INPUT1.splitlines()]
    print(calc_turns(INPUT1))

    INPUT2 = load_input(2025, 4, 2)
    INPUT2 = [int(n) for n in INPUT2.splitlines()]
    print(calc_min_turns(INPUT2))

    INPUT3 = load_input(2025, 4, 3)
    INPUT3 = [[int(n) for n in line.split("|")] for line in INPUT3.splitlines()]
    print(calc_turns_coupled(INPUT3))
