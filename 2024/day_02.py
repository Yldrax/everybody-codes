""" Second Day"""

import re

def quest_1(input_str: str):
    total = 0
    text = input_str.splitlines()[2]
    words = input_str.splitlines()[0]
    words = words.split(":")
    words = words[1].split(",")

    for w in words:
        x = re.findall(f"{w}" ,text)
        total += len(x)
    return total

def quest_2(input_str: str):
    text = input_str.splitlines()[2:]
    words = input_str.splitlines()[0]
    words = words.split(":")
    words = words[1].split(",")
    runes = []
    for i, subtext in enumerate(text):
        runes.append([])
        # Array to not count glyphs multiple times
        for _ in subtext:
            runes[i].append(False)
        
    for i, subtext in enumerate(text):
        for word in words:
            if word == subtext or word[::-1] == subtext:
                runes[i] = [True for char in subtext]
            elif len(word) >= len(subtext):
                continue

            for j in range(len(subtext)-len(word)):
                pass
                
            


    total = sum(val for row in runes for val in row)
    return total

if __name__ == "__main__":
    from utils import load_input
    INPUT1 = load_input(2024, 2, 1)
    print(quest_1(INPUT1))
    INPUT2 = load_input(2024, 2, 2)
    #print(quest_2(INPUT2))
    #INPUT3 = load_input(2024, 2, 3)

    teststring = """WORDS:THE,OWE,MES,ROD,HER,QAQ

AWAKEN THE POWE ADORNED WITH THE FLAMES BRIGHT IRE
THE FLAME SHIELDED THE HEART OF THE KINGS
POWE PO WER P OWE R
THERE IS THE END
QAQAQ"""

    print(quest_2(teststring))

    