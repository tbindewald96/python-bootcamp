# Import necessary modules and lists

import random
from hangman_words import words
from hangman_art import stages
from hangman_art import logo


# Chose word from wordlist and determine length of word

word = random.choice(words)

# turn word into list 

word_list = []

for letter in word:
    word_list.append(letter)

print(word_list)

# Create a placeholder 

solution_list = []

for letter in word_list:
    solution_list.append("_")

print(solution_list)

# Create a count with initial lives

lives = 7

# Create a list for wrong guesses

guesses = []

# Show Hangman Logo

print(logo)
# Game runs until complete word is guessed

while not (solution_list == word_list or lives == 0):
    print(stages[lives])
    guess = input("Guess a letter:\n").lower()
    counter = 0
# If correct letter is guessed, swap correct placeholders with guessed letters
    for letter in word_list:
        if guess == word_list[counter]:
            solution_list[counter] = guess
        counter += 1
# If wrong letter is guessed remove one live from counter and print respective hangman step
    if guess not in word_list and guess not in guesses:
        guesses.append(guess)
        lives -= 1

# Print current solution list
    print(solution_list)
    print(guesses)
    print(lives)

# Print either solution or last hangman

solution = ''.join(solution_list)

if solution_list == word_list:
    print(solution)
    print("You won!")
elif lives == 0:
    print(stages[lives])
    print("You lost!")

