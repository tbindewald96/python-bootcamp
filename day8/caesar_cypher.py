alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(encode_or_decode, original_text, shift_amount):
    text = ""
    for letter in original_text:
        if encode_or_decode == "encode":
            location = alphabet.index(letter) + shift_amount
        elif encode_or_decode == "decode":
            location = alphabet.index(letter) - shift_amount
        location %= len(alphabet) 
        text += alphabet[location]
    print(f"Here is the {encode_or_decode} result: {text}")

caesar(encode_or_decode, text, shift)
