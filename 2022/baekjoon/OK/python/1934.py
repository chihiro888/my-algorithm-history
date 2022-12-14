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
# 최대공약수
def gcd(a, b):  
    while b > 0:
        a, b = b, a % b
    return a


# 최소공배수
def lcm(a, b):
    return a * b / gcd(a, b)
# -------------------------------


# Please write the code below ---
def main():
    t = int(ip())
    for _ in range(t):
        a, b = mv(int)
        print(int(lcm(a, b)))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------