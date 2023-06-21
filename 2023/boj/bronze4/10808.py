import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
# 문자열을 리스트로 변환
def str_to_list(s:str):
    return [x for x in s]

# 알파벳 넣고 인덱스 반환
def get_alphabet_index(char):
    char = char.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    if char in alphabet:
        return alphabet.index(char)
    else:
        return -1
    
# 리스트를 문자열로 출력
def print_list(l: list):
    print(' '.join(map(str, l)))
# -------------------------------


# Please write the code below ---
def main():
    s = ip()
    s = str_to_list(s)
    d = [0] * 26
    for x in s:
        idx = get_alphabet_index(x)
        d[idx] += 1
    
    print_list(d)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------