"""Sixth Day"""

from utils import load_input


def calc_sword_pairs(notes: str) -> int:
    total = 0
    mentors = 0
    for n in notes:
        match n:
            case "A":
                mentors += 1
            case "a":
                total += mentors
    return total


def calc_pairs(notes: str) -> int:
    total = 0
    sword = 0
    archery = 0
    magic = 0
    for n in notes:
        match n:
            case "A":
                sword += 1
            case "B":
                archery += 1
            case "C":
                magic += 1
            case "a":
                total += sword
            case "b":
                total += archery
            case "c":
                total += magic
    return total


def calc_pattern_pairs(notes: str) -> int:
    length = len(notes)
    pattern = notes * 3
    first_count = [0 for _ in range(length)]
    mid_count = [0 for _ in range(length)]
    last_count = [0 for _ in range(length)]

    for i, char in enumerate(notes):
        if char == char.lower():
            mid_count[i] = pattern[length + i - 1000 : length + i + 1001].count(
                char.upper()
            )
            first_count[i] = pattern[
                max(length + i - 1000, length) : length + i + 1001
            ].count(char.upper())
            last_count[i] = pattern[
                length + i - 1000 : min(length + i + 1001, 2 * length)
            ].count(char.upper())

    total = sum(first_count) + 998 * sum(mid_count) + sum(last_count)
    return total


if __name__ == "__main__":
    INPUT1 = load_input(2025, 6, 1)
    print(calc_sword_pairs(INPUT1))

    INPUT2 = load_input(2025, 6, 2)
    print(calc_pairs(INPUT2))

    INPUT3 = load_input(2025, 6, 3)
    print(calc_pattern_pairs(INPUT3))
