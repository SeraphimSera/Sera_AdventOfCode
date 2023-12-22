from collections import Counter
from typing import Literal
from functools import cmp_to_key


with open("2023/Day 7/day7_data.txt", 'r') as f:
    lines: list[str] = f.readlines()

lines = {k: v for k, v in [l.strip().split() for l in lines]}
total_win: int = 0


class HandP1:
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    def compare_hand(self, c1: str, c2: str) -> Literal[1, -1]:
        """
        Compares two given hands and 
        Returns 1 if c1 is stronger than c2,
        Otherwise returns -1.
        """

        sorted_c1 = self.sorted_counter(c1)
        sorted_c2 = self.sorted_counter(c2)

        if self.find_kind(sorted_c1) == self.find_kind(sorted_c2):
            return self.compare_kind(c1, c2)

        return 1 if self.find_kind(sorted_c1) > self.find_kind(sorted_c2) else -1

    @staticmethod
    def sorted_counter(cards: str) -> tuple[str, int]:
        return sorted(
            Counter(cards).items(), 
            key=lambda c: c[1],
            reverse=True
        )


    def compare_kind(self, c1_k: str, c2_k: str) -> Literal[1, -1]:
        """
        Iterates over each card set
        To find which set is stronger.
        """

        for k1, k2 in zip(c1_k, c2_k):
            if self.cards.index(k1) != self.cards.index(k2):
                return 1 if self.cards.index(k1) > self.cards.index(k2) else -1
    

    @staticmethod
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


# Part 1
card_values = sorted(
    lines, 
    key=cmp_to_key(HandP1().compare_hand)
)

print(sum(
    [int(lines[i[1]])*i[0] for i in enumerate(card_values, start=1)]
))


# Part 2
class HandP2(HandP1):
    cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


    @staticmethod
    def sorted_counter(cards: str) -> tuple[str, int]:
        # too lazy to properly handle edge cases lmfao
        if cards == "JJJJJ":
            return [('J', 5)]

        cards: dict[str, int] = dict(Counter(cards))

        # Find jokered cards, spoof them into highest value ones
        if 'J' in cards:
            j_value = cards.pop('J')
            highest_value = sorted(
                cards.items(), 
                key=lambda c: c[1],
                reverse=True
            )[0][0]
            cards[highest_value] = cards[highest_value] + j_value

        return sorted(
            cards.items(), 
            key=lambda c: c[1],
            reverse=True
        )

card_values = sorted(
    lines, 
    key=cmp_to_key(HandP2().compare_hand)
)

print(sum(
    [int(lines[i[1]])*i[0] for i in enumerate(card_values, start=1)]
))
