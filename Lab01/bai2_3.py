import random
import re
from collections import Counter
import string
import copy

# --- 1. TỪ ĐIỂN ĐÁNH GIÁ (Bộ não đầy đủ của chương trình) ---
ENG_FREQ = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
COMMON_WORDS = {
    'THE', 'AND', 'OF', 'TO', 'A', 'IN', 'IS', 'THAT', 'IT', 'WAS', 'FOR', 'ON', 'ARE', 
    'WITH', 'AS', 'I', 'HIS', 'THEY', 'BE', 'AT', 'ONE', 'HAVE', 'THIS', 'FROM', 'OR', 'HAD', 
    'BY', 'HOT', 'WORD', 'BUT', 'WHAT', 'SOME', 'WE', 'CAN', 'OUT', 'OTHER', 'WERE', 'ALL', 
    'THERE', 'WHEN', 'UP', 'USE', 'YOUR', 'HOW', 'SAID', 'AN', 'EACH', 'SHE', 'WHICH', 'DO', 
    'THEIR', 'TIME', 'IF', 'WILL', 'WAY', 'ABOUT', 'MANY', 'THEN', 'THEM', 'WRITE', 'WOULD'
}
COMMON_BIGRAMS = ['TH', 'HE', 'IN', 'ER', 'AN', 'RE', 'ND', 'AT', 'ON', 'NT', 'HA', 'ES', 'ST', 'EN', 'ED', 'TO', 'IT', 'OU', 'EA', 'HI']
COMMON_TRIGRAMS = ['THE', 'AND', 'THA', 'ENT', 'ION', 'TIO', 'FOR', 'NDE', 'HAS', 'NCE', 'EDT', 'TIS', 'OFT', 'STH', 'MEN']

def calculate_fitness(text):
    """Chấm điểm bản rõ dựa trên từ vựng tiếng Anh chuẩn."""
    score = 0
    text_upper = text.upper()
    words = text_upper.split()
    
    for w in words:
        clean_w = re.sub(r'[^A-Z]', '', w)
        if clean_w in COMMON_WORDS:
            score += len(clean_w) * 100 
            
    for bg in COMMON_BIGRAMS:
        score += text_upper.count(bg) * 10
    for tg in COMMON_TRIGRAMS:
        score += text_upper.count(tg) * 30
        
    return score

# --- 2. THUẬT TOÁN GIẢI MÃ ---
def apply_key(text, key):
    """Dịch văn bản theo chìa khóa hiện tại."""
    result = []
    for c in text:
        if c.islower(): result.append(key.get(c.upper(), c.upper()).lower())
        elif c.isupper(): result.append(key.get(c, c))
        else: result.append(c)
    return "".join(result)

def solve_cipher(ciphertext):
    """Sử dụng Hill Climbing để tìm ra chìa khóa tối ưu nhất."""
    # Tạo chìa khóa khởi tạo dựa trên phân tích tần suất
    cipher_letters = re.sub(r'[^A-Z]', '', ciphertext.upper())
    counts = Counter(cipher_letters)
    sorted_chars = [pair[0] for pair in counts.most_common()]
    for char in string.ascii_uppercase:
        if char not in sorted_chars:
            sorted_chars.append(char)
            
    best_overall_key = dict(zip(sorted_chars, ENG_FREQ))
    best_overall_score = calculate_fitness(apply_key(ciphertext, best_overall_key))
    best_overall_text = ""

    # Leo đồi với 15 lần khởi động lại
    for restart in range(15):
        current_key = copy.deepcopy(best_overall_key)
        
        # Xáo trộn nhẹ chìa khóa nếu không phải vòng đầu tiên
        if restart > 0:
            keys = list(current_key.keys())
            for _ in range(5):
                a, b = random.sample(keys, 2)
                current_key[a], current_key[b] = current_key[b], current_key[a]
                
        current_score = calculate_fitness(apply_key(ciphertext, current_key))
        no_improve = 0
        
        for _ in range(3000):
            # Tráo 2 chữ cái ngẫu nhiên
            new_key = copy.deepcopy(current_key)
            keys = list(new_key.keys())
            c1, c2 = random.sample(keys, 2)
            new_key[c1], new_key[c2] = new_key[c2], new_key[c1]
            
            new_score = calculate_fitness(apply_key(ciphertext, new_key))
            
            if new_score > current_score:
                current_score, current_key = new_score, new_key
                no_improve = 0
            else:
                no_improve += 1
                
            if no_improve > 500: # Cắt sớm nếu không thể leo cao hơn
                break
                
        if current_score > best_overall_score:
            best_overall_score = current_score
            best_overall_key = current_key
            best_overall_text = apply_key(ciphertext, current_key)

    if not best_overall_text:
        best_overall_text = apply_key(ciphertext, best_overall_key)
        
    return best_overall_text, best_overall_key

# --- 3. GIAO DIỆN CHÍNH ---
def main():
    print("=== GIẢI MÃ MONO-ALPHABETIC SUBSTITUTION ===")
    print("1. Nhập ciphertext trực tiếp")
    print("2. Đọc ciphertext từ file (Copy Path từ VS Code)")
    choice = input("-> Chọn (1 hoặc 2): ")

    text = ""
    if choice == '1':
        print("\nDán văn bản vào đây (Gõ chữ DONE ở một dòng mới rồi Enter để bắt đầu):")
        lines = []
        while (line := input().strip()) != "DONE":
            lines.append(line)
        text = "\n".join(lines)
    elif choice == '2':
        path = input("\nDán đường dẫn file vào đây: ").strip('\"\' ')
        try:
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
        except Exception as e:
            return print(f"Lỗi không mở được file: {e}")
    else:
        return print("Lựa chọn không hợp lệ!")

    if not text.strip():
        return print("Văn bản rỗng!")

    print("\n[+] Đang giải mã bằng Hill Climbing, vui lòng đợi vài giây...")
    plaintext, best_key = solve_cipher(text)
    
    print("\n" + "="*60)
    print(" KẾT QUẢ GIẢI MÃ TỐT NHẤT")
    print("="*60)
    print(plaintext)
    print("="*60)
    
    print("\n[ CHÌA KHÓA TÌM ĐƯỢC (Cipher -> Plain) ]")
    # In chìa khóa thành 2 hàng cho gọn đẹp
    items = sorted(best_key.items())
    half = len(items) // 2
    for i in range(half):
        k1, v1 = items[i]
        k2, v2 = items[i + half]
        print(f" {k1} -> {v1} \t|\t {k2} -> {v2} ")
    print()

if __name__ == "__main__":
    main()