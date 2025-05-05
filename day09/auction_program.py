from art import logo

print(logo)

bids = {}
list_of_bids = []
max_value = 0

auction = True

print("Welcome to the auction.")

while auction:
    name = input("Enter your name.\n")
    bid = int(input("Enter your bid.\n"))
    bids[name] = bid
    another = input("Is there another bidder? Type 'yes' or 'no'.\n").lower()
    if another == "yes":
        auction = True
    elif another == "no":
        auction = False
    print("\n"*100)

for name, bid in bids.items():
     if bid > max_value:
         winner = name
         highest_bid = bid

print(f"The winner is {winner} with a bid of ${highest_bid}.")




