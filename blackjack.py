#!/usr/bin/env python3
import random


class deck:
    def __init__(self, number_of_decks=1):
        self.number_of_decks = number_of_decks
        self.quantity = 52 * number_of_decks


class card:
    def __init__(self):
        self.suit = random.choice(suit)
        self.rank = random.choice(rank)
        self.card = deck[self.suit][self.rank]

class hand:
    def __init__(self):
        self.handle = []

    def add_card(self, card):
        self.handle.append(card)

    def score():
        pass

    def __str__(self):
        show_me = []
        for card in self.handle:
            show_me.append(chr(card.card))
            show_me.append("   ")
        return "".join(show_me)


suit = ["Spades", "Hearts", "Diamonds", "Clubs"]
rank = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
        "Nine", "Ten", "Jack", "Queen", "King"]


spade = {rank[0]: 0x1F0A1, rank[1]: 0x1F0A2, rank[2]: 0x1F0A3, rank[3]: 0x1F0A4,
         rank[4]: 0x1F0A5, rank[5]: 0x1F0A6, rank[6]: 0x1F0A7, rank[7]: 0x1F0A8,
         rank[8]: 0x1F0A9, rank[9]: 0x1F0AA, rank[10]: 0x1F0AB, rank[11]: 0x1F0AD,
         rank[12]: 0x1F0AE} 

heart = {rank[0]: 0x1F0B1, rank[1]: 0x1F0B2, rank[2]: 0x1F0B3, rank[3]: 0x1F0B4,
         rank[4]: 0x1F0B5, rank[5]: 0x1F0B6, rank[6]: 0x1F0B7, rank[7]: 0x1F0B8,
         rank[8]: 0x1F0B9, rank[9]: 0x1F0BA, rank[10]: 0x1F0BB, rank[11]: 0x1F0BD,
         rank[12]: 0x1F0BE} 

diamo = {rank[0]: 0x1F0C1, rank[1]: 0x1F0C2, rank[2]: 0x1F0C3, rank[3]: 0x1F0C4,
         rank[4]: 0x1F0C5, rank[5]: 0x1F0C6, rank[6]: 0x1F0C7, rank[7]: 0x1F0C8,
         rank[8]: 0x1F0C9, rank[9]: 0x1F0CA, rank[10]: 0x1F0CB, rank[11]: 0x1F0CD,
         rank[12]: 0x1F0CE} 

clubs = {rank[0]: 0x1F0D1, rank[1]: 0x1F0D2, rank[2]: 0x1F0D3, rank[3]: 0x1F0D4,
         rank[4]: 0x1F0D5, rank[5]: 0x1F0D6, rank[6]: 0x1F0D7, rank[7]: 0x1F0D8,
         rank[8]: 0x1F0D9, rank[9]: 0x1F0DA, rank[10]: 0x1F0DB, rank[11]: 0x1F0DD,
         rank[12]: 0x1F0DE} 

deck = {"Spades": spade, "Hearts": heart, "Diamonds": diamo, "Clubs": clubs}

def main():

    alpha = hand()
    x = card()
    y = card()
    alpha.add_card(x)
    alpha.add_card(y)
    print(alpha)

    while True:
        response = input("Hit? ")
        if response is 'Y':
            z = card()
            alpha.add_card(z)
            print(alpha)
        else:
            print("RUHROH")
            break


if __name__ == '__main__':
    main()
