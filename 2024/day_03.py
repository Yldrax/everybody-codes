""" Third Day"""

def dig_down(map: list[str]):
    depth = 0
    while True:
        changed = False
        for x in range(1, len(map)-1):
            for y in range(1,len(map[0])-1):
                current = map[x][y]
                if current == '#' or current.isnumeric():
                    localdepth = 0 if current == '#' else int(current)
                    #check all four directions


        if not changed:
            break




if __name__ == "__main__":
    from utils import load_input
    INPUT1 = load_input(2024, 3, 1)
    INPUT1 = INPUT1.splitlines()