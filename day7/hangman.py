import random

# chose word from wordlist and determine length of word

list = ["aardvark", "baboon", "camel"]

word = random.choice(list)

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

# Game runs until complete word is guessed


while solution_list != word_list:
    guess = input("Guess a letter:\n").lower()
    counter = 0
# If correct letter is guessed, swap correct placeholders with guessed letters
    for letter in word_list:
        if guess == word_list[counter]:
            solution_list[counter] = guess
        counter += 1
    print(solution_list)

# Once complete word was guessed, join list and print solution
    
solution = ''.join(solution_list)

print(solution)





