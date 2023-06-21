import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
# 자리수 출력 제한
def format_float(n: float):
    return "{:.2f}".format(n)
# -------------------------------


# Please write the code below ---
def main():
    while True:
        n = float(ip())

        if n == 0:
            break
    
        a = 1
        b = n
        c = n * n
        d = n * n * n
        e = n * n * n * n

        print(format_float(round(a+b+c+d+e, 2)))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------