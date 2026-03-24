from Crypto.Cipher import DES

def to_bin(data):
    return bin(int.from_bytes(data, 'big'))[2:].zfill(64)

def hamming_distance(b1, b2):
    return sum(x != y for x, y in zip(b1, b2))

def avalanche_test(key):
    p1 = b'STAYHOME'
    p2 = b'STAYHOMA'# Chỉ khác 1 ký tự cuối so với p1
    cipher = DES.new(key, DES.MODE_ECB)
    c1 = cipher.encrypt(p1)
    c2 = cipher.encrypt(p2)
    b1 = to_bin(c1)
    b2 = to_bin(c2)
    diff = hamming_distance(b1, b2)
    percent = diff / 64 * 100

    print("Key:", key)
    print("Cipher 1:", b1)
    print("Cipher 2:", b2)
    print("Different bits:", diff)
    print("Avalanche %:", percent, "%")
    print("-" * 40)

keys = [
    b'87654321',
    b'24521599',
    b'24521691',
    b'24521840'
]

for k in keys:
    avalanche_test(k)