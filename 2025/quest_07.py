"""Seventh Day"""

from utils import load_input


# Helper Functions
def get_names(notes: str) -> list[str]:
    return notes.splitlines()[0].split(",")


def get_rules(notes: str) -> dict[str, list[str]]:
    ruledict = {}
    rules = notes.splitlines()[2:]
    for rule in rules:
        followers = rule[4:].split(",")
        ruledict[rule[0]] = followers
    return ruledict


def check_name(name: str, rules: dict[str, list[str]]) -> bool:
    for i in range(len(name) - 1):
        if name[i + 1] not in rules[name[i]]:
            return False
    return True


# 1
def find_name(notes: str) -> str:
    names = get_names(notes)
    rules = get_rules(notes)
    for name in names:
        if check_name(name, rules):
            return name
    return "Error"


# 2
def find_name_sum(notes: str) -> int:
    total = 0
    names = get_names(notes)
    rules = get_rules(notes)
    for i, name in enumerate(names):
        if check_name(name, rules):
            total += i + 1
    return total


# 3
def build_names(notes: str) -> int:
    prefixes = [name for name in get_names(notes) if check_name(name, get_rules(notes))]
    rules = get_rules(notes)

    def add_letters(name: str) -> set[str]:
        names = set()
        if 7 <= len(name) <= 11:
            names.add(name)
        if len(name) == 11:
            return names

        for letter in rules.get(name[-1], []):
            names |= add_letters(name + letter)

        return names

    total_names = set()
    for prefix in prefixes:
        total_names |= add_letters(prefix)

    return len(total_names)


if __name__ == "__main__":
    INPUT1 = load_input(2025, 7, 1)
    print(find_name(INPUT1))

    INPUT2 = load_input(2025, 7, 2)
    print(find_name_sum(INPUT2))

    INPUT3 = load_input(2025, 7, 3)
    print(build_names(INPUT3))
