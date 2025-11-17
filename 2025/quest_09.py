"""Ninth Day"""

from itertools import combinations
from utils import load_input


def compare_ducks(duck1: str, duck2: str) -> int:
    similarity = 0
    for i, j in zip(duck1, duck2):
        if i == j:
            similarity += 1
    return similarity


def calc_similarity(notes: list[str] | tuple[str, str, str]) -> int:
    parent1 = 0
    parent2 = 0
    for p1, p2, c in zip(*notes):
        if p1 == c:
            parent1 += 1
        if p2 == c:
            parent2 += 1
        if c not in (p1, p2):
            return -1
    return parent1 * parent2


def find_calc_similarities(notes: list[str]) -> int:
    total = 0

    parents = list(combinations(notes, 2))
    for child in notes:
        for parent_pair in parents:
            if child not in parent_pair:
                similarity = calc_similarity((*parent_pair, child))
                if similarity != -1:
                    total += similarity
    return total


if __name__ == "__main__":
    INPUT1 = [s.split(":")[1] for s in load_input(2025, 9, 1).splitlines()]
    print(calc_similarity(INPUT1))

    INPUT2 = [s.split(":")[1] for s in load_input(2025, 9, 2).splitlines()]
    print(find_calc_similarities(INPUT2))
