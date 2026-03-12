def input_key():
    while True:
        key = input("Enter key (letters only A-Z): ")
        if key.isalpha():
            return key.upper()
        print("Invalid key! Only letters A-Z allowed.")

def generate_key(text, key):
    key_extended = ""
    j = 0
    for c in text:
        if c.isalpha():
            key_extended += key[j % len(key)]
            j += 1
        else:
            key_extended += c
    return key_extended

def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = generate_key(plaintext, key)
    ciphertext = ""
    for p, k in zip(plaintext, key):
        if p.isalpha():
            c = (ord(p) - 65 + ord(k) - 65) % 26
            ciphertext += chr(c + 65)
        else:
            ciphertext += p
    return ciphertext

def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = generate_key(ciphertext, key)
    plaintext = ""
    for c, k in zip(ciphertext, key):
        if c.isalpha():
            p = (ord(c) - 65 - (ord(k) - 65) + 26) % 26
            plaintext += chr(p + 65)
        else:
            plaintext += c
    return plaintext

while True:
    print("\n1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        text = input("Enter plaintext: ")
        key = input_key()
        print("Ciphertext:", encrypt(text, key))
    elif choice == "2":
        text = input("Enter ciphertext: ")
        key = input_key()
        print("Plaintext:", decrypt(text, key))
    elif choice == "3":
        break