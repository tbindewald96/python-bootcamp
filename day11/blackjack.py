from art import logo

import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

input("Do you want to play a game of blackjack? Type 'y' or 'n': ")

player_cards = []
dealer_cards = []

# first round 

for count in (0,1):
    player_cards.append(random.choice(cards))

dealer_cards.append(random.choice(cards))


print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
print(f"Computer's first card: {dealer_cards}")

input("Type 'y' to get another card, type 'n' to pass: ")

player_cards.append(random.choice(cards))

