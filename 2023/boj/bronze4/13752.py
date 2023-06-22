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
    t = int(ip())
    for _ in range(t):
        n = int(ip())
        for _ in range(n):
            print('=', end='')
        print()
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------