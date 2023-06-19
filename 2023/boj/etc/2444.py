import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def print_pattern(n):
    for i in range(n):
        for _ in range(n - i - 1):
            print(" ", end="")
        for _ in range(2 * i + 1):
            print("*", end="")
        print()

    for i in range(n - 2, -1, -1):
        for _ in range(n - i - 1):
            print(" ", end="")
        for _ in range(2 * i + 1):
            print("*", end="")
        print()
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