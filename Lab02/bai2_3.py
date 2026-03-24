from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

BLOCK_SIZE = 16

plaintext = get_random_bytes(1000)

def pad(data):
    pad_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([pad_len]) * pad_len

plaintext_padded = pad(plaintext)

key = get_random_bytes(16)
iv = get_random_bytes(16)

def show_error_blocks(original, modified):
    blocks = len(original) // BLOCK_SIZE
    error_list = []
    print("\nBlock comparison:")
    print("-" * 40)
    for i in range(blocks):
        b1 = original[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE]
        b2 = modified[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE]
        if b1 != b2:
            error_list.append(i)
            status = "ERROR"
        else:
            status = "OK"
        print(f"Block {i:02d}: {status}")
    print("-" * 40)
    print(f"==> Tổng block lỗi: {len(error_list)}")
    print(f"==> Các block lỗi: {error_list}")

def test_mode(name, mode_enc, mode_dec):
    print(f"\n========== {name} ==========")

    ciphertext = mode_enc.encrypt(plaintext_padded)
    corrupted = bytearray(ciphertext)
    corrupted[25] ^= 0x01
    corrupted = bytes(corrupted)

    decrypted = mode_dec.decrypt(corrupted)

    show_error_blocks(plaintext_padded, decrypted)

test_mode(
    "ECB",
    AES.new(key, AES.MODE_ECB),
    AES.new(key, AES.MODE_ECB)
)

test_mode(
    "CBC",
    AES.new(key, AES.MODE_CBC, iv),
    AES.new(key, AES.MODE_CBC, iv)
)

test_mode(
    "CFB",
    AES.new(key, AES.MODE_CFB, iv, segment_size=128),
    AES.new(key, AES.MODE_CFB, iv, segment_size=128)
)

test_mode(
    "OFB",
    AES.new(key, AES.MODE_OFB, iv),
    AES.new(key, AES.MODE_OFB, iv)
)