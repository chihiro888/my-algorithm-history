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
    s = ip()
    s = str_to_list(s)
    if s.count('M') > 0 and s.count('O') > 0 and s.count('B') > 0 and s.count('I') > 0 and s.count('S') > 0:
        print('YES')
    else:
        print('NO')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------