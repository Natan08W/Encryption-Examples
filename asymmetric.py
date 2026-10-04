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

import string
import random

def getRandKey(): # Keys are currently simple and reversible, this needs to be changed to a more complex and secure key generation method in the future
    letters = list(string.ascii_uppercase)
    shuffled = letters.copy()
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled))

class Node():
    def __init__(self):
        self.__publicKey = bidict(getRandKey())
        self.__privateKey = self.__publicKey.inverse

    def encrypt(self, message, target):
        encryptedMessage = ""
        for char in message.upper():
            if char in target.getPublicKey():
                encryptedMessage += "".join(self.__privateKey[target.getPublicKey()[char]]) # Plaintext -> Target's Public Key -> Sender's Private Key -> Ciphertext
            else:
                encryptedMessage += char
        return encryptedMessage

    def decrypt(self, message, sender):
        decryptedMessage = ""
        for char in message.upper():
            if char in sender.getPublicKey().inverse:
                decryptedMessage += "".join(self.__privateKey["".join(sender.getPublicKey()[char])]) # Ciphertext -> Sender's Public Key -> Target's Private Key -> Plaintext
            else:
                decryptedMessage += char
        return decryptedMessage

    def getPublicKey(self):
        return self.__publicKey

Anna = Node()
Bob = Node()

while True:
    sender = input("Who is sending the message? (Anna/Bob): ").capitalize()
    if sender not in ["Anna", "Bob"]:
        print("Invalid sender. Please enter 'Anna' or 'Bob'.")
        continue
    receiver = "Bob" if sender == "Anna" else "Anna"
    message = input(f"Enter the message to send from {sender} to {receiver}: ")
    if sender == "Anna":
        encryptedMessage = Anna.encrypt(message, Bob)
        print(f"Encrypted message from Anna to Bob: {encryptedMessage}")
        decryptedMessage = Bob.decrypt(encryptedMessage, Anna)
        print(f"Decrypted message at Bob's end: {decryptedMessage}")
    else:
        encryptedMessage = Bob.encrypt(message, Anna)
        print(f"Encrypted message from Bob to Anna: {encryptedMessage}")
        decryptedMessage = Anna.decrypt(encryptedMessage, Bob)
        print(f"Decrypted message at Anna's end: {decryptedMessage}")