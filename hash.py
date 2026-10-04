import hashlib

def hash(message, salt, hashMode = "sha256"):
    if hashMode == "sha256":
        return hashlib.sha256((message + salt).encode()).hexdigest()
    elif hashMode == "md5":
        return hashlib.md5((message + salt).encode()).hexdigest()
    elif hashMode == "custom":
        result = 0
        for char in message + salt:
            result += ord(char)
            result = (result * 31) % (2**32)
        return hex(result)[2:]  # Return the hash as a hexadecimal string
    else:
        raise ValueError("Unsupported hash mode. Use 'sha256' or 'md5'.")

while True:
    message = input("Enter the message to hash: ")
    salt = input("Enter the salt: ")
    hashMode = input("Enter the hash mode (sha256/md5/custom): ").lower()
    try:
        hashedMessage = hash(message, salt, hashMode)
        print(f"Hashed message ({hashMode}):", hashedMessage)
    except ValueError as e:
        print(e)