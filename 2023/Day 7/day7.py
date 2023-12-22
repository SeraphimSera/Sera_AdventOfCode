from collections import Counter
from typing import Literal
from functools import cmp_to_key

with open("2023/Day 7/day7_data.txt", 'r') as f:
    lines: list[str] = f.readlines()

lines = {k: v for k, v in [l.strip().split() for l in lines]}
cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

total_win: int = 0
def compare_hand(c1: str, c2: str) -> Literal[1, -1]:
    """
    Compares two given hands and 
    Returns 1 if c1 is stronger than c2,
    Otherwise returns -1.
    """

    def sorted_counter(cards: str) -> tuple[str, int]:
        return sorted(
            Counter(cards).items(), 
            key=lambda c: c[1],
            reverse=True
        )


    def compare_kind(c1_k: str, c2_k: str) -> Literal[1, -1]:
        """
        Iterates over each card set
        To find which set is stronger.
        """

        for k1, k2 in zip(c1_k, c2_k):
            if cards.index(k1) == cards.index(k2):
                continue
            return 1 if cards.index(k1) > cards.index(k2) else -1
    

    def find_kind(cards: list[tuple[str, int]]) -> int:
        """
        Gives each card set a value
        based on what kind of set it is.
        """

        if cards[0][1] == 3:
            # Full house
            if cards[1][1] == 2:
                return 4
            # Three of a kind
            return 3
        elif cards[0][1] == 2:
            # Two pair
            if cards[1][1] == 2:
                return 2
            # One pair
            return 1
        # High card
        elif all([c[1] == 1 for c in cards]):
            return 0
        return cards[0][1] + 1  
    

    sorted_c1 = sorted_counter(c1)
    sorted_c2 = sorted_counter(c2)

    if find_kind(sorted_c1) == find_kind(sorted_c2):
        return compare_kind(c1, c2)

    return 1 if find_kind(sorted_c1) > find_kind(sorted_c2) else -1


# Part 1
card_values = sorted(
    lines, 
    key=cmp_to_key(compare_hand)
)

print(sum(
    [int(lines[i[1]])*i[0] for i in enumerate(card_values, start=1)]
))