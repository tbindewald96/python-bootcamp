print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L:\n")
pepperoni = input("Do you want pepperoni on your pizza? Y or N:\n")
extra_cheese = input("Do you want extra cheese? Y or N:\n")
total = 0
if size == "S":
    total += 15
elif size == "M":
    total += 20
elif size == "L":
    total += 25
else:
    print("You typed a wrong input.")

if pepperoni == "Y":
    if size == "S":
        total += 2
    else:
        total += 3

if extra_cheese == "Y":
    total += 1

print(f"Your total bill is ${total}.")

