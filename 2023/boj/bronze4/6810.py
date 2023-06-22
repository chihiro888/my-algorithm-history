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
    return [int(x) for x in s]
# -------------------------------


# Please write the code below ---
def main():
    s = [int(ip()) for _ in range(3)]
    r = 9 * 1 + 7 * 3 + 8 * 1 + 0 * 3 + 9 * 1 + 2 * 3 + 1 * 1 + 4 * 3 + 1 * 1 + 8 * 3 + s[0] * 1 + s[1] * 3 + s[2] * 1
    print(f'The 1-3-sum is {r}')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------