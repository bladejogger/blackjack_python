#!/usr/bin/env python3
import random
import sys

class card:
    def __init__(self):
        self.suit = random.choice(suit)
        self.rank = random.choice(rank)
        self.card = deck[self.suit][self.rank]
        try:
            self.point = int(self.rank)
        except Exception:
            if self.rank == "Ace":
                self.point = 1
            else:
                self.point = 10


class hand:
    def __init__(self):
        self.handle = []

    def add_card(self, card):
        self.handle.append(card)

    def validate(self, check, quant):
        check = card
        neo = card()
        while check in self.handle and self.handle.count(z) == quant:
            neo = card()
        return neo

    def score(self):
        tally = 0
        for x in self.handle:
            tally += x.point
        return tally

    def __str__(self):
        show_me = []
        for card in self.handle:
            show_me.append(chr(card.card))
            show_me.append("   ")
        return "".join(show_me)


suit = ["Spades", "Hearts", "Diamonds", "Clubs"]
rank = ["Ace", "2", "3", "4", "5", "6", "7", "8", 
        "9", "10", "Jack", "Queen", "King"]

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
    please = ["Y", "y", "yes", "YES", "Yes"]
    thanks = ["N", "n", "no", "NO", "No", "Stay", "STAY", "stay"]

    while True:
        try:
            number_decks = int(input("Enter number of decks (1 - 7): "))
        except Exception:
            print("I'm sorry, Dave...  I can't allow you to do that.")
            continue
        if number_decks > 0 and number_decks < 8:
            break

    alpha = hand()
    x = card()
    y = card()
    while y == x and number_decks == 1:
        y = card()
    alpha.add_card(x)
    alpha.add_card(y)
    print(alpha)

    while alpha.score() < 22:
        response = input("Hit? ")
        if response in please:
            z = card()
            alpha.validate(z, number_decks)
            alpha.add_card(z)
            print(alpha)
        elif response in thanks:
            winrar = alpha.score()
            print(winrar)
            print("decent...")
            sys.exit()
        else:
            print("RUHROH")
            sys.exit()

    print("BUUUUSTED!!!")

if __name__ == '__main__':
    main()
