"""Eighth Day"""

from collections import defaultdict
from itertools import combinations
from utils import load_input
from tqdm import tqdm


def calc_center(notes: list[int]) -> int:
    total = 0
    for i in range(len(notes) - 1):
        if abs(notes[i] - notes[i + 1]) == 16:
            total += 1
    return total


def check_intersection(l1: tuple[int, int], l2: tuple[int, int]) -> bool:
    a, b = l1
    c, d = l2
    if a < c < b < d or b < c < a < d or c < a < d < b or d < a < c < b:
        return True
    return False


def calc_knots(notes: list[int]) -> int:
    total = 0
    strings = defaultdict(int)
    for i in range(len(notes) - 1):
        new_string = (min(notes[i], notes[i + 1]), max(notes[i], notes[i + 1]))
        strings[new_string] += 1

        for string, amount in strings.items():
            if check_intersection(string, new_string):
                total += amount

    return total


def calc_best_strike(notes: list[int]) -> int:
    best_strike = 0
    strings = defaultdict(int)
    strikes = combinations(range(1, 257), 2)

    for i in range(len(notes) - 1):
        new_string = (min(notes[i], notes[i + 1]), max(notes[i], notes[i + 1]))
        strings[new_string] += 1

    for strike in tqdm(list(strikes)):
        current_strike = 0
        for string in strings:
            if check_intersection(strike, string):  # type: ignore
                current_strike += 1
        current_strike = (
            current_strike + strings[strike] if strike in strings else current_strike
        )
        best_strike = max(best_strike, current_strike)

    return best_strike


if __name__ == "__main__":
    INPUT1 = [int(n) for n in load_input(2025, 8, 1).split(",")]
    print(calc_center(INPUT1))

    INPUT2 = [int(n) for n in load_input(2025, 8, 2).split(",")]
    print(calc_knots(INPUT2))

    INPUT3 = [int(n) for n in load_input(2025, 8, 3).split(",")]
    print(calc_best_strike(INPUT3))
