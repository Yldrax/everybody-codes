"""Fifth Day"""

from utils import load_input
from typing import Union
from dataclasses import dataclass
import re


@dataclass
class bone:
    spine: int
    left: Union[int, None] = None
    right: Union[int, None] = None


@dataclass
class sword:
    id: int
    quality: int
    fishbone: list[bone]


def create_fishbone(numbers: list[int]) -> list[bone]:
    # Ignore First Number in First Task
    bones = [bone(numbers[1])]
    for n in numbers[2:]:
        for b in bones:
            if n < b.spine and b.left is None:
                b.left = n
                break
            if n > b.spine and b.right is None:
                b.right = n
                break
        else:
            bones.append(bone(n))
    return bones


def calc_quality(numbers: list[int]) -> int:
    fishbone = create_fishbone(numbers)
    quality = ""
    for f in fishbone:
        quality += str(f.spine)
    return int(quality)


def calc_level_qualites(fishbone: list[bone]) -> tuple[int]:
    qualities = []
    for b in fishbone:
        q = ""
        q += str(b.left) if b.left is not None else ""
        q += str(b.spine)
        q += str(b.right) if b.right is not None else ""
        qualities.append(int(q))
    return tuple(qualities)


def calc_max_difference(swords: list[list[int]]) -> int:
    qualities = [calc_quality(s) for s in swords]
    return max(qualities) - min(qualities)


def calc_checksum(swords: list[list[int]]) -> int:
    sword_list = []
    for s in swords:
        sword_list.append(sword(s[0], calc_quality(s), create_fishbone(s)))
    sword_list.sort(
        reverse=True, key=lambda x: (x.quality, calc_level_qualites(x.fishbone), x.id)
    )
    checksum = 0
    for i, s in enumerate(sword_list):
        checksum += s.id * (i + 1)
    return checksum


if __name__ == "__main__":
    INPUT1 = load_input(2025, 5, 1)
    INPUT1 = [int(n) for n in re.split(r",|:", INPUT1)]
    print(calc_quality(INPUT1))

    INPUT2 = load_input(2025, 5, 2)
    INPUT2 = [[int(n) for n in re.split(r",|:", m)] for m in INPUT2.splitlines()]
    print(calc_max_difference(INPUT2))

    INPUT3 = load_input(2025, 5, 3)
    INPUT3 = INPUT3 = [
        [int(n) for n in re.split(r",|:", m)] for m in INPUT3.splitlines()
    ]
    print(calc_checksum(INPUT3))
