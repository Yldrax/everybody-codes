"""Stuff used for more than one day"""

def get_input(day: int, part: int):
    """Read the Input form the text file"""
    with open(f"2024/inputs/{day:02d}_{part}.txt", 'r', encoding = "utf-8") as f:
        text = f.read()

    return text
