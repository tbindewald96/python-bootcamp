# Import necessary modules and lists

import random
from hangman_words import words
from hangman_art import stages, logo

# Chose word from wordlist and determine length of word

word = random.choice(words)

# turn word into list 

word_list = []

for letter in word:
    word_list.append(letter)

# Create a placeholder 

solution_list = []

for letter in word_list:
    solution_list.append("_")

# Create a count with initial lives

lives = 7

# Create a list for wrong guesses

guesses = []

# Show Hangman Logo

print(logo)

# Show length of word

solution = ''.join(solution_list)
print(f"The word we are lookin for is {solution}")
solution_list = list(solution)

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
    if guess in guesses:
        print(f"You already guessed {guess}")
    if guess not in word_list and guess not in guesses:
        guesses.append(guess)
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a live.")

# Print current solution list
    solution = ''.join(solution_list)
    print(f"The word we are looking for is {solution}")
    solution_list = list(solution)

# Print either solution or last hangman

solution = ''.join(solution_list)

if solution_list == word_list:
    print(solution)
    print("You won!")
elif lives == 0:
    print(stages[lives])
    print("You lost!")

