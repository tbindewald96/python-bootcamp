from art import logo

import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
dealer_cards = []
blackjack = True

def sum_on_hand(party):
    return sum(party)

x = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")

while blackjack == True:
    if x == "y":
        for count in (0,1):
            player_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
        print(f"Your cards: {player_cards}, current score: {sum_on_hand(player_cards)}")
        print(f"Computer's first card: {dealer_cards}")



input("Type 'y' to get another card, type 'n' to pass: ")



