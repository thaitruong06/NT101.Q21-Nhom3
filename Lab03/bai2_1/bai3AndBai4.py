import base64

def char_to_num(c):
    # 'a'-'z' -> 00-25
    if 'a' <= c <= 'z':
        return ord(c) - ord('a')
    # 'A'-'Z' -> 26-51
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 26
    return ord(c) + 100 

def num_to_char(n):
    if 0 <= n <= 25:
        return chr(n + ord('a'))
    if 26 <= n <= 51:
        return chr(n - 26 + ord('A'))
    return chr(n - 100)

def solve_task_3():
    print("\n--- CÂU 3: MÃ HÓA THÔNG ĐIỆP ---")
    p = int(input("Nhập p: "), 0)
    q = int(input("Nhập q: "), 0)
    e = int(input("Nhập e: "), 0)
    msg = input("Nhập thông điệp: ")
    
    n = p * q
    
    encoded_blocks = []
    for char in msg:
        m = char_to_num(char)
        c = pow(m, e, n)
        c_bytes = c.to_bytes((c.bit_length() + 7) // 8 or 1, byteorder='big')
        c_base64 = base64.b64encode(c_bytes).decode('utf-8')
        encoded_blocks.append(c_base64)
    
    final_result = ",".join(encoded_blocks)
    print(f"Bản mã gộp (Base64): {final_result}")

def solve_task_4():
    print("\n--- CÂU 4: GIẢI MÃ BẢN MÃ ---")
    p = int(input("Nhập p: "), 0)
    q = int(input("Nhập q: "), 0)
    e = int(input("Nhập e: "), 0)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    
    print("Chọn định dạng bản mã nhập vào:")
    print("1. Base64 (các block cách nhau bởi dấu phẩy)")
    print("2. Hex")
    print("3. Nhị phân")
    choice = input("Lựa chọn (1/2/3): ")
    cipher_input = input("Nhập bản mã: ")

    decrypted_msg = ""
    
    if choice == '1':
        blocks = cipher_input.split(',')
        for b64_block in blocks:
            c_bytes = base64.b64decode(b64_block)
            c = int.from_bytes(c_bytes, byteorder='big')
            m = pow(c, d, n)
            decrypted_msg += num_to_char(m)
            
    elif choice == '2':
        c = int(cipher_input, 16)
        m = pow(c, d, n)
        m_str = str(m).zfill(2)
        if len(m_str) % 2 != 0: m_str = '0' + m_str
        for i in range(0, len(m_str), 2):
            val = int(m_str[i:i+2])
            decrypted_msg += num_to_char(val)

    elif choice == '3':
        c = int(cipher_input, 2)
        m = pow(c, d, n)
        m_str = str(m).zfill(2)
        for i in range(0, len(m_str), 2):
            val = int(m_str[i:i+2])
            decrypted_msg += num_to_char(val)

    print(f"Bản rõ sau khi giải mã: {decrypted_msg}")

if __name__ == "__main__":
    mode = input("Bạn muốn làm câu 3 hay 4? (nhập 3 hoặc 4): ")
    if mode == '3':
        solve_task_3()
    elif mode == '4':
        solve_task_4()