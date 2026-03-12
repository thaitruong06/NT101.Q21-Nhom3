def create_matrix(key):
    key = key.upper().replace("J","I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    used = ""
    for c in key + alphabet:
        if c.isalpha() and c not in used:
            used += c

    matrix = [list(used[i:i+5]) for i in range(0,25,5)]
    return matrix


def print_matrix(matrix):
    print("\nPlayfair Matrix:")
    for row in matrix:
        print(" ".join(row))


def find_pos(matrix, c):
    if c == "J":
        c = "I"
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == c:
                return i, j


def prepare_text(text):
    text = text.upper().replace("I", "J").replace(" ", "")
    prepared = ""
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 < len(text):
            b = text[i + 1]

            if a == b:
                prepared += a + "X"
                i += 1
            else:
                prepared += a + b
                i += 2
        else:
            prepared += a + "X"
            i += 1

    return prepared


def encrypt(text, matrix):
    text = prepare_text(text)
    cipher = ""

    for i in range(0,len(text),2):
        a,b = text[i], text[i+1]
        r1,c1 = find_pos(matrix,a)
        r2,c2 = find_pos(matrix,b)

        if r1 == r2:
            cipher += matrix[r1][(c1+1)%5]
            cipher += matrix[r2][(c2+1)%5]

        elif c1 == c2:
            cipher += matrix[(r1+1)%5][c1]
            cipher += matrix[(r2+1)%5][c2]

        else:
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher


def decrypt(text, matrix):
    text = text.upper()
    plain = ""

    for i in range(0,len(text),2):
        a,b = text[i], text[i+1]
        r1,c1 = find_pos(matrix,a)
        r2,c2 = find_pos(matrix,b)

        if r1 == r2:
            plain += matrix[r1][(c1-1)%5]
            plain += matrix[r2][(c2-1)%5]

        elif c1 == c2:
            plain += matrix[(r1-1)%5][c1]
            plain += matrix[(r2-1)%5][c2]

        else:
            plain += matrix[r1][c2]
            plain += matrix[r2][c1]

    return plain



mode = input("Nhap P de ma hoa, C de giai ma: ").upper()
key = input("Nhap key: ")

matrix = create_matrix(key)
print_matrix(matrix)

if mode == "P":
    plaintext = input("Nhap plaintext: ")
    print("Ciphertext:", encrypt(plaintext, matrix))

elif mode == "C":
    ciphertext = input("Nhap ciphertext: ")
    print("Plaintext:", decrypt(ciphertext, matrix))

else:
    print("Lua chon khong hop le")