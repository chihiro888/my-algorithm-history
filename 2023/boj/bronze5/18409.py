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
# -------------------------------


# Please write the code below ---
def main():
    x = int(ip())
    s = ip()
    s = str_to_list(s)
    print(s.count('a') + s.count('i') + s.count('u') + s.count('e') + s.count('o'))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------