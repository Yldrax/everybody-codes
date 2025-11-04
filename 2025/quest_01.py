"""First Day"""


def find_name(input_str: str):
    names, _empty, moves = input_str.splitlines()
    names = names.split(",")
    moves = moves.split(",")
    current = 0
    max_length = len(names) - 1
    for m in moves:
        if "L" in m:
            current -= int(m[1])
            current = max(current, 0)
        else:
            current += int(m[1])
            current = min(current, max_length)
    return names[current]


def find_first_parent(input_str: str):
    names, _empty, moves = input_str.splitlines()
    names = names.split(",")
    moves = moves.split(",")
    current = 0
    max_length = len(names)
    for m in moves:
        if "L" in m:
            current = (current - int(m[1:3])) % max_length
        else:
            current = (current + int(m[1:3])) % max_length
    return names[current]


def find_second_parent(input_str: str):
    names, _empty, moves = input_str.splitlines()
    names = names.split(",")
    moves = moves.split(",")
    max_length = len(names)

    for m in moves:
        if "L" in m:
            x = -int(m[1:3]) % max_length
            names[0], names[x] = names[x], names[0]
        else:
            x = int(m[1:3]) % max_length
            names[0], names[x] = names[x], names[0]

    return names[0]


if __name__ == "__main__":
    from utils import load_input

    INPUT1 = load_input(2025, 1, 1)
    print(find_name(INPUT1))

    INPUT2 = load_input(2025, 1, 2)
    print(find_first_parent(INPUT2))

    INPUT3 = load_input(2025, 1, 3)
    print(find_second_parent(INPUT3))
