letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = range(1, 10)

import random

print("Welcome to the PyPassword Generator!.")
nr_letters = int(input("How many letters would you like in your passsword?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

list_of_letters = []
list_of_symbols = []
list_of_numbers = []
random_list = []


for i in range(0, nr_letters):
    l = str(letters[random.randint(0, len(letters))-1])
    list_of_letters.append(l)

for i in range(0, nr_symbols):
    s = str(symbols[random.randint(0, len(symbols))-1])
    list_of_symbols.append(s)

for i in range(0, nr_numbers):
    n = str(numbers[random.randint(0, len(numbers))-1])
    list_of_numbers.append(n)

final_list = list_of_letters + list_of_symbols + list_of_numbers

random.shuffle(final_list)

password = ''.join(final_list)

print(f"Your password is: {password}")