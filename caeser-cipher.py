def translateByKey(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a') # Shift the character and wrap around the alphabet
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)
        else: # Non-alphabetic characters are not changed
            result += char

    return result

mode = input("Would you like to encrypt or decrypt a message? (E/D): ").upper()
message = input("Enter the message: ")
key = int(input("Enter the key: "))
if mode == "D": key = -key
print("Result:", translateByKey(message, key))