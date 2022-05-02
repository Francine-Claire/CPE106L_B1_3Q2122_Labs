import random
import cardDeck
import card.py
import player
import pile

def play_war(pile):
    player_a = pile[:len(pile)/2]
    player_b = pile[len(pile)/2:]
    a_stash = []
    b_stash = []

    round = 1
    while a_cards and b_cards:
            a_card = a_cards.pop()
            b_card = b_cards.pop()

            if a_card == b_card:
                a_stash.extend([a_card]+a_cards[-3:])
                a_cards = a_cards[:-3]
                a_cards.append(a_stash.pop())

                b_stash.extend([b_card]+b_cards[-3:])
                b_cards = b_cards[:-3]
                b_cards.append(b_stash.pop())
            elif a_card > b_card:
                a_cards = [a_card, b_card] + a_stash + b_stash + a_cards
                a_stash = []
                b_stash = []
            elif b_card > a_card:
                b_cards = [b_card, a_card] + b_stash + a_stash + b_cards
                a_stash = []
                b_stash = []

            print (round, len(a_cards), len(a_stash), len(b_cards), len(b_stash))
            round += 1
    if __name__ == '__main__':
        play_war(pile)