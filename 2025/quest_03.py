"""Third Day"""

from collections import Counter


def stack_crates(ls: list[int]) -> int:
    unique_crates = set(ls)
    return sum(unique_crates)


def pack_mushroom(ls: list[int]) -> int:
    unique_crates = list(set(ls))
    return sum(unique_crates[:20])


def minimize_sets(ls: list[int]) -> int:
    _, sets = Counter(ls).most_common(1)[0]
    return sets


if __name__ == "__main__":
    from utils import load_input

    INPUT1 = load_input(2025, 3, 1)
    INPUT1 = [int(n) for n in INPUT1.split(",")]
    print(stack_crates(INPUT1))

    INPUT2 = load_input(2025, 3, 2)
    INPUT2 = [int(n) for n in INPUT2.split(",")]
    print(pack_mushroom(INPUT2))

    INPUT3 = load_input(2025, 3, 3)
    INPUT3 = [int(n) for n in INPUT3.split(",")]
    print(minimize_sets(INPUT3))
