import sys


# Utilities ---------------------
debug = False
def p(name, value):
    if debug: print(f'{name} = {value}')
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
# -------------------------------


# Function Block ----------------
# 문자열을 리스트로 변환
def str_to_list(s:str):
    return [x for x in s]
# -------------------------------


# Please write the code below ---
def main():
    t = int(ip())
    s = ip()
    s = str_to_list(s)
    if s.count('A') > s.count('B'):
        print('A')
    elif s.count('A') < s.count('B'):
        print('B')
    else:
        print('Tie')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------