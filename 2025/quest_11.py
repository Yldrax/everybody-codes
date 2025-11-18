"""Eleventh Day"""

from utils import load_input


def balance_formation(notes: list[int], maxrounds: int):
    formation = notes.copy()
    phase = 1
    balanced = False
    rounds = 0
    while not balanced and (rounds < maxrounds or maxrounds == -1):
        if rounds % 250000 == 0:
            print(rounds)
        rounds += 1
        changed = False
        if phase == 1:
            for i in range(len(formation) - 1):
                if formation[i] > formation[i + 1]:
                    formation[i] -= 1
                    formation[i + 1] += 1
                    changed = True
            if not changed:
                phase = 2

        if phase == 2:
            for i in range(len(formation) - 1):
                if formation[i] < formation[i + 1]:
                    formation[i] += 1
                    formation[i + 1] -= 1
                    changed = True
            if not changed:
                balanced = True

    checksum = 0
    for i, line in enumerate(formation):
        checksum += (i + 1) * line

    return (checksum, rounds - 1)


if __name__ == "__main__":
    INPUT1 = [int(n) for n in load_input(2025, 11, 1).splitlines()]
    print(balance_formation(INPUT1, 10)[0])

    INPUT2 = [int(n) for n in load_input(2025, 11, 2).splitlines()]
    print(balance_formation(INPUT2, -1)[1])

    INPUT3 = [int(n) for n in load_input(2025, 11, 3).splitlines()]
    # print(balance_formation(INPUT3, -1)[1])    #Way too inefficient
