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

# 리스트를 문자열로 출력
def print_list(l: list):
    print(''.join(map(str, l)))
# -------------------------------


# Please write the code below ---
def main():
    while True:
        s = ip()
        if s == 'END':
            break
        x = str_to_list(s)
        x.reverse()
        print_list(x)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------