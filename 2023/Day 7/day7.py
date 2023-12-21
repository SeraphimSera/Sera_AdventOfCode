from collections import Counter
from typing import Literal
from functools import cmp_to_key

with open("2023/Day 7/day7_data.txt", 'r') as f:
    lines: list[str] = f.readlines()

lines = [l.strip().split() for l in lines]
cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

total_win: int = 0
def compare_hand(c1: str, c2: str) -> Literal[1, -1]:
    """
    Compares two given hands and 
    Returns 1 if c1 is stronger than c2,
    Otherwise returns -1.
    """

    def compare_kind(c1_k: str, c2_k: str) -> Literal[1, -1]:
        """
        Iterates over each card set
        To find which set is stronger.
        """

        for k1, k2 in zip(c1_k, c2_k):
            if k2.index(cards) > k1.index(cards):
                return -1
        return 1

    c1_count = Counter(c1)
    c2_count = Counter(c2)

    match max(c1_count.values()):
        # Five of a kind
        case 5:
            if max(c2_count.values()) == 5 and cards.index(c2[0]) > cards.index(c1[0]):
                return -1
            return 1

        # Four of a kind
        case 4:

        # Full house, three of a kind
        case 3:

        # Two pair, one pair
        case 2:

        # High card
        case _:
        

print(Counter(lines[0][0]).keys())