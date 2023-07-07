import sys
from itertools import permutations

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
    n = ip()
    n = sorted(n, reverse=True)
    sum = 0
    if '0' not in n:
        print(-1)
    else:
        for i in n:
            sum += int(i)
        if sum % 3 != 0:
            print(-1)
        else:
            print("".join(n))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------