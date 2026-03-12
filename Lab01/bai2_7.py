def encrypt_rail_fence(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]

    dir_down = False
    row, col = 0, 0

    for char in text:
        if row == 0 or row == key - 1:
            dir_down = not dir_down

        rail[row][col] = char
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])

    return "".join(result)


def decrypt_rail_fence(cipher, key):
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]

    dir_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    return "".join(result)



print("=== Rail Fence Cipher ===")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Choose option (1/2): ")

key = int(input("Enter key (number of rails): "))

if choice == "1":
    plaintext = input("Enter plaintext: ").upper().replace(" ", "")
    ciphertext = encrypt_rail_fence(plaintext, key)
    print("Ciphertext:", ciphertext)

elif choice == "2":
    ciphertext = input("Enter ciphertext: ").upper().replace(" ", "")
    plaintext = decrypt_rail_fence(ciphertext, key)
    print("Plaintext:", plaintext)

else:
    print("Invalid choice!")