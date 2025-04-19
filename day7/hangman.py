import random

# Step 1:

word_list = ["aardvark", "baboon", "camel"]

word = random.choice(word_list)

placeholder = ""

print(word)

for letter in word:
    placeholder += "_"

print(placeholder)

# Step 2: 

guess = input("Guess a letter:\n").lower()

# Step 3: 

count = -1
for letter in word:
    count += 1
    if guess == letter:
        placeholder_list = list(placeholder)
        placeholder_list[count] = guess
        placeholder = ''.join(placeholder_list)

print(placeholder)






