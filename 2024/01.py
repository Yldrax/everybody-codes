"""First Day"""


# 1
def calc_monster(monster: str) -> int:
    """Calc Potiosn for a single Monster"""
    match monster:
        case "A":
            return 0
        case "B":
            return 1
        case "C":
            return 3
        case "D":
            return 5
        case "x":
            return 0


def calc_potions1(input_str: str) -> int:
    """Calculate needed Potions"""
    total = 0
    for i in input_str:
        total += calc_monster(i)

    return total


# 2
def calc_potions2(input_str: str) -> int:
    """Calculate needed Potions"""
    total = 0
    for i in range(0, len(input_str), 2):
        pair = input_str[i : i + 2] 
        total += calc_monster(pair[0])
        total += calc_monster(pair[1])
        if "x" not in pair:
            total += 2
    return total

#3
def calc_potions3(input_str: str) -> int:
    """Calculate needed Potions"""
    total = 0
    for i in range(0, len(input_str), 3):
        trio = input_str[i : i + 3] 
        total += calc_monster(trio[0])
        total += calc_monster(trio[1])
        total += calc_monster(trio[2])
        x = trio.count("x")
        if x == 0:
            total += 6
        elif x == 1:
            total += 2
    return total

if __name__ == "__main__":
    from utils import get_input

    INPUT1 = get_input(1, 1)
    INPUT2 = get_input(1, 2)
    INPUT3 = get_input(1, 3)
    print(calc_potions1(INPUT1))
    print(calc_potions2(INPUT2))
    print(calc_potions3(INPUT3))
