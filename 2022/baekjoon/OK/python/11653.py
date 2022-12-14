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
# 소인수분해
def factorization(x):
    d = 2

    while d <= x:
        if x % d == 0:
            print(d)
            x = x / d
        else:
            d = d + 1
# -------------------------------


# Please write the code below ---
def main():
    n = int(ip())
    factorization(n)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------