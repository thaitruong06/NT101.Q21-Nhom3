def caesar_cipher(text, key, mode='encrypt'):
    """
    Thực hiện mã hóa hoặc giải mã bằng Caesar Cipher.
    """
    result = ""
    # Nếu là giải mã, ta dịch chuyển ngược lại (trừ đi key)
    if mode == 'decrypt':
        key = -key
        
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            # Dịch chuyển ký tự và xử lý vòng lặp bảng chữ cái (Modulo 26)
            shifted = (ord(char) - ascii_offset + key) % 26
            result += chr(shifted + ascii_offset)
        else:
            # Giữ nguyên các ký tự không phải là chữ cái (dấu câu, khoảng trắng...)
            result += char
    return result

def brute_force_caesar(ciphertext):
    """
    Thực hiện brute-force và tự động tìm bản rõ đúng nhất 
    dựa trên việc đếm các từ tiếng Anh phổ biến.
    """
    # Tập hợp các từ tiếng Anh thông dụng để nhận diện bản rõ
    common_words = {'the', 'is', 'a', 'and', 'in', 'of', 'to', 'for', 'with', 'on', 'at', 'by', 'an', 'this', 'it', 'under'}
    
    best_score = 0
    best_key = 0
    best_plaintext = ""
    
    # Thử toàn bộ 25 khóa có thể
    for key in range(1, 26):
        decrypted = caesar_cipher(ciphertext, key, mode='decrypt')
        
        # Tách từ (loại bỏ dấu câu) để đối chiếu
        clean_words = ''.join(c if c.isalpha() else ' ' for c in decrypted).lower().split()
        
        # Chấm điểm dựa trên số lượng từ tiếng Anh có nghĩa
        score = sum(1 for word in clean_words if word in common_words)
        
        # Cập nhật kết quả nếu tìm thấy bản rõ có điểm cao hơn
        if score > best_score:
            best_score = score
            best_key = key
            best_plaintext = decrypted
            
    return best_key, best_plaintext

# ==========================================
# PHẦN CHẠY THỬ NGHIỆM
# ==========================================
if __name__ == "__main__":
    print("--- 1. MÃ HÓA & GIẢI MÃ TÙY CHỈNH ---")
    # Uncomment các dòng dưới đây nếu bạn muốn chạy tương tác nhập từ bàn phím
    # mode = input("Chọn chế độ (encrypt/decrypt): ").strip().lower()
    # text = input("Nhập văn bản: ")
    # key = int(input("Nhập khóa (số nguyên): "))
    # print(f"Kết quả: {caesar_cipher(text, key, mode)}\n")
    
    print("--- 2. GIẢI MÃ ĐOẠN VĂN BẢN (BRUTE-FORCE TỰ ĐỘNG) ---")
    ciphertext = """Max NBM bl t extwbgz bglmbmnmbhg ngwxk OGN-AVF, lixvbtebsbgz bg max ybxew hy bgyhkftmbhg mxvaghehzr. Xlmtueblaxw pbma t fbllbhg mh yhlmxk bgghotmbhg tgw xqvxeexgvx bg BM xwnvtmbhg tgw kxlxtkva, NBM hyyxkl t pbwx ktgzx hy ngwxkzktwntmx tgw ihlmzktwntmx ikhzktfl tbfxw tm ikhwnvbgz abzaer ldbeexw ikhyxllbhgtel. Max ngboxklbmr bl kxvhzgbsxw yhk bml vnmmbgz-xwzx kxlxtkva bg tkxtl ebdx vruxklxvnkbmr, tkmbybvbte bgmxeebzxgvx, tgw lhymptkx xgzbgxxkbgz. Pbma lmtmx-hy-max-tkm ytvbebmbxl tgw t lmkhgz xfiatlbl hg vheetuhktmbhg pbma bgwnlmkr, NBM xjnbil lmnwxgml pbma uhma maxhkxmbvte dghpexwzx tgw iktvmbvte ldbeel mh makbox bg max ktibwer xoheobgz mxva bgwnlmkr."""
    
    found_key, plaintext = brute_force_caesar(ciphertext)
    
    print(f"[*] Khóa mã hóa (Encryption Key) đã được sử dụng: {found_key}")
    print(f"[*] Để giải mã, ta dịch chuyển lùi lại {found_key} bước (hoặc tiến lên {26 - found_key} bước).")
    print("\n[*] BẢN RÕ (PLAINTEXT) ĐÃ ĐƯỢC GIẢI MÃ:\n")
    print(plaintext)