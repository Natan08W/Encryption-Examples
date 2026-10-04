def translateByKey(message, key):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a') # Shift the character and wrap around the alphabet
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)
        else: # Non-alphabetic characters are not changed
            result += char
    return result

while True:
    mode = input("Would you like to encrypt or decrypt a message? (E/D): ").upper()
    message = input("Enter the message: ")
    key = int(input("Enter the key: "))
    if mode == "D": key = -key # Negate the key for decryption
    print("Result:", translateByKey(message, key))