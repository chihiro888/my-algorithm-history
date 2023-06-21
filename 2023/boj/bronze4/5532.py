import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------

# -------------------------------


# Please write the code below ---
def main():
    l = int(ip())
    a = int(ip()) # 국어
    b = int(ip()) # 수학
    c = int(ip()) # 일일 국어
    d = int(ip()) # 일일 수학

    if a % c == 0:
        x = (a // c)
    else:
        x = (a // c) + 1

    if b % d == 0:
        y = (b // d)
    else:
        y = (b // d) + 1

    print(l - max(x, y))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------