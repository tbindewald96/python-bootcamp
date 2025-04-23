alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

def encrypt(original_text, shift_amount):

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
    original_text_list = list(original_text)
    count = 0
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
    for letter in original_text_list:
        location = alphabet.index(letter) + shift
        if location > len(alphabet)-1:
            location %= len(alphabet) 
        original_text_list[count] = alphabet[location]
        count += 1
        original_text = ''.join(original_text_list)
    print(f"Here is the encoded result: {original_text}")

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.

def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letter in original_text:
        location = alphabet.index(letter) - shift_amount
        decrypted_text += alphabet[location]
    print(f"Here is the decoded result: {decrypted_text}")

# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
