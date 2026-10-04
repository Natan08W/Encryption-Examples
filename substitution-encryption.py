# Bidict library not working so stole this code from stackoverflow, goated.
# Source - https://stackoverflow.com/a/21894086
# Posted by Basj, modified by community. See post 'Timeline' for change history
# Retrieved 2026-10-04, License - CC BY-SA 4.0

class bidict(dict):
    def __init__(self, *args, **kwargs):
        super(bidict, self).__init__(*args, **kwargs)
        self.inverse = {}
        for key, value in self.items():
            self.inverse.setdefault(value, []).append(key) 

    def __setitem__(self, key, value):
        if key in self:
            self.inverse[self[key]].remove(key) 
        super(bidict, self).__setitem__(key, value)
        self.inverse.setdefault(value, []).append(key)        

    def __delitem__(self, key):
        self.inverse.setdefault(self[key], []).remove(key)
        if self[key] in self.inverse and not self.inverse[self[key]]: 
            del self.inverse[self[key]]
        super(bidict, self).__delitem__(key)
# End of stolen code

substitution_cipher = bidict({"A": "Q", "B": "W", "C": "E", "D": "R", "E": "T", "F": "Y", "G": "U", "H": "I", "I": "O", "J": "P",
                               "K": "A", "L": "S", "M": "D", "N": "F", "O": "G", "P": "H", "Q": "J", "R": "K", "S": "L", "T": "Z", "U": "X", "V": "C", "W": "V",
                               "X": "B", "Y": "N", "Z": "M",}) # Values can be changed to any other letter, but must be unique

while True:
    choice = input("Would you like to encrypt or decrypt a message? (E/D): ").upper()
    if choice == "E":
        message = input("Enter the message to encrypt: ").upper()
        encrypted_message = ""
        for char in message:
            if char in substitution_cipher:
                encrypted_message += substitution_cipher[char]
            else:
                encrypted_message += char
        print("Encrypted message:", encrypted_message)
    elif choice == "D":
        message = input("Enter the message to decrypt: ").upper()
        decrypted_message = ""
        for char in message:
            if char in substitution_cipher.inverse:
                decrypted_message += "".join(substitution_cipher.inverse[char])
            else:
                decrypted_message += char
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")