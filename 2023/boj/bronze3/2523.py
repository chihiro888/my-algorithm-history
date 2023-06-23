import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def print_pattern(n):
    for i in range(1, n+1):
        stars = '*' * i
        print(stars)
    for i in range(n-1, 0, -1):
        stars = '*' * i
        print(stars)
# -------------------------------


# Please write the code below ---
def main():
    n = int(ip())
    print_pattern(n)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------