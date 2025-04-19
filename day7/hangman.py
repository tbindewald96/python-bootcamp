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

# If correct letter is guessed, swap correct placeholders with guessed letters
    for letter in word_list:
        location = word_list.index(letter)
        print(location)


#solution = ''.join(solution_list)





