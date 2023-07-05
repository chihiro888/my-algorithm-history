import sys
import math

# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
# 팩토리얼
def factorial(n):
    return math.factorial(n)
# -------------------------------


# Please write the code below ---
def main():
    size = int(ip())
    for _ in range(size):
        n, m = mv(int)
        print(factorial(m) // (factorial(n) * factorial(m - n)))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------