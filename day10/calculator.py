from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
    }

calculation = True

n1 = float(input("Whats the first number?\n"))
for symbol in operations:
    print(symbol)
operator = input("What is the operation?\n")
n2 = float(input("What is the second number?\n"))

while calculation == True:
    print(f"The result of {n1} {operator} {n2} is {operations[operator](n1, n2)}")
    n1 = float(operations[operator](n1, n2))
    continue_calculation = input("Do you want to continue to calculate with this number? Type yes or no.\n").lower()
    if continue_calculation == "yes":
        operator = input("What is the next operation?\n")
        n2 = float(input("What is the next number?\n"))
    else:
        n1 = 0
        n1 = float(input("Whats the first number?\n"))
        operator = input("What is the operation?\n")
        n2 = float(input("What is the second number?\n"))
        