alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        location = alphabet.index(letter) + shift
        if location > len(alphabet)-1:
            location %= len(alphabet) 
        encrypted_text += alphabet[location]
    print(f"Here is the encoded result: {encrypted_text}")

def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letter in original_text:
        location = alphabet.index(letter) - shift_amount
        if 0 > location and location > -len(alphabet):
            location = len(alphabet) + location
        decrypted_text += alphabet[location]
        if -len(alphabet) > location:
            location %= len(alphabet)


    print(f"Here is the decoded result: {decrypted_text}")


# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
