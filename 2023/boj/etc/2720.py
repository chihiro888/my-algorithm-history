import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def solution(x):
    # q d n p
    q = 0
    d = 0
    n = 0
    p = 0

    if x >= 25:
        q = x // 25
        x = x % 25

    if x >= 10:
        d = x // 10
        x = x % 10

    if x >= 5:
        n = x // 5
        x = x % 5

    if x >= 1:
        p = x // 1
        x = x % 1

    print(f'{q} {d} {n} {p}')
# -------------------------------


# Please write the code below ---
def main():
    size = int(ip())
    for _ in range(size):
        d = int(ip())
        solution(d)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------