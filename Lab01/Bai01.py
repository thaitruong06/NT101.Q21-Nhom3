def caesar_cipher(text, key, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        key = -key
        
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted = (ord(char) - ascii_offset + key) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char
            
    return result


def brute_force_caesar(ciphertext):
    common_words = {
        'the', 'is', 'a', 'and', 'in', 'of', 'to', 'for',
        'with', 'on', 'at', 'by', 'an', 'this', 'it', 'under'
    }

    best_score = 0
    best_key = 0
    best_plaintext = ""

    for key in range(1, 26):
        decrypted = caesar_cipher(ciphertext, key, mode='decrypt')

        clean_words = ''.join(
            c if c.isalpha() else ' ' for c in decrypted
        ).lower().split()

        score = sum(1 for word in clean_words if word in common_words)

        if score > best_score:
            best_score = score
            best_key = key
            best_plaintext = decrypted

    return best_key, best_plaintext


text = input("Nhập plain text: ")
mode = input("Chọn chế độ (1: Caesar, 2: Brute force): ")

if mode == "1":
    k = int(input("Nhập k: "))
    action = input("Chọn encrypt/decrypt: ").lower()
    result = caesar_cipher(text, k, action)
    print(result)

elif mode == "2":
    key, plaintext = brute_force_caesar(text)
    print(f"Key: {key}")
    print(plaintext)