"""Second Day"""

from tqdm import tqdm


def add(num1: tuple[int, int], num2: tuple[int, int]) -> tuple[int, int]:
    x1, y1 = num1
    x2, y2 = num2
    return (x1 + x2, y1 + y2)


def multiply(num1: tuple[int, int], num2: tuple[int, int]) -> tuple[int, int]:
    x1, y1 = num1
    x2, y2 = num2
    return (x1 * x2 - y1 * y2, x1 * y2 + y1 * x2)


def divide(num1: tuple[int, int], num2: tuple[int, int]) -> tuple[int, int]:
    x1, y1 = num1
    x2, y2 = num2
    q0 = x1 // x2 if x1 >= 0 else -(-x1 // x2)
    q1 = y1 // y2 if y1 >= 0 else -(-y1 // y2)
    return (q0, q1)


def calculate1(A: tuple[int, int]) -> tuple[int, int]:
    R = (0, 0)
    for _ in range(3):
        R = multiply(R, R)
        R = divide(R, (10, 10))
        R = add(R, A)
    return R


def calc_point(coords: tuple[int, int]) -> bool:
    """calc if point should be engraved"""
    R = (0, 0)
    for _ in range(100):
        R = multiply(R, R)
        R = divide(R, (100000, 100000))
        R = add(R, coords)
        if any(abs(num) > 1000000 for num in R):
            return False
    return True


def calculate2(A: tuple[int, int]) -> int:
    total = 0
    for y in range(101):
        for x in range(101):
            if calc_point(add(A, (x * 10, y * 10))):
                total += 1
    return total


def calculate3(A: tuple[int, int]) -> int:
    total = 0
    for y in tqdm(range(1001)):
        for x in range(1001):
            if calc_point(add(A, (x, y))):
                total += 1
    return total


if __name__ == "__main__":
    from utils import load_input

    INPUT1 = load_input(2025, 2, 1)
    print(calculate1((166, 52)))

    INPUT2 = load_input(2025, 2, 2)
    print(calculate2((-79785, 15616)))

    INPUT3 = load_input(2025, 2, 3)
    print(calculate3((-79785, 15616)))
