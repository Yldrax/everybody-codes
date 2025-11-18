"""Tenth Day"""

from copy import deepcopy
from utils import load_input


def check_range(notes: list[str]) -> int:
    total = 0
    grid = [["." for _ in range(len(row))] for row in notes]
    grid[len(grid) // 2][len(grid[0]) // 2] = "D"
    for _ in range(4):
        new_grid = deepcopy(grid)
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                if col == "D":
                    for yoffset, xoffset in [
                        (2, 1),
                        (2, -1),
                        (-2, 1),
                        (-2, -1),
                        (1, 2),
                        (1, -2),
                        (-1, 2),
                        (-1, -2),
                    ]:
                        try:
                            new_grid[y + yoffset][x + xoffset] = "D"
                        except IndexError:
                            pass
        grid = new_grid

    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "D" and notes[y][x] == "S":
                total += 1
    return total


if __name__ == "__main__":
    INPUT1 = load_input(2025, 10, 1).splitlines()
    print(check_range(INPUT1))
