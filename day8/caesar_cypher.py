from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(encode_or_decode, original_text, shift_amount):
    text = ""
    for letter in original_text:
        if encode_or_decode == "encode":
            if letter in alphabet:
                location = alphabet.index(letter) + shift_amount
                location %= len(alphabet) 
                text += alphabet[location]
            else: 
                text += letter
        elif encode_or_decode == "decode":
            if letter in alphabet:
                location = alphabet.index(letter) - shift_amount
                location %= len(alphabet) 
                text += alphabet[location]
            else:
                text += letter
    print(f"Here is the {encode_or_decode} result: {text}")

run = True

while run:
    encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(encode_or_decode, text, shift)
    decision = input("Do you want to continue? Type yes or no.\n").lower()
    if decision == "yes":
        run = True
    elif decision == "no": 
        run = False

print("Thank you for using Caesar Cipher!")

