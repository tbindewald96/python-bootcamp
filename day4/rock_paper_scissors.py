import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

x = random.randint(0, 2)
y = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if y == 0:
    print(rock)
    if x == 0:
        print(f"The computer chose:\n{rock}")
        print("Draw.")
    elif x ==1:
        print(f"The computer chose:\n{paper}")
        print("You lose!")
    else:
        print(f"The computer chose:\n{scissors}")
        print("You win!")
elif y == 1:
    print(paper)
    if x == 0:
        print(f"The computer chose:\n{rock}")
        print("You win!")
    elif x == 1:
        print(f"The computer chose:\n{paper}")
        print("Draw.")
    else:
        print(f"The computer chose:\n{scissors}")
        print("You lose!")
elif y == 2:
    print(scissors)
    if x == 0:
        print(f"The computer chose:\n{rock}")
        print("You lose!")
    elif x ==1:
        print(f"The computer chose:\n{paper}")
        print("You win!")
    else:
        print(f"The computer chose:\n{scissors}")
        print("Draw.")
else:
    print("You typed in an invalid number. You lose!")
