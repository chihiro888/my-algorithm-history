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
    while True:
        try:
            n, s = mv(int)
            print(s // (n + 1))
        except BaseException:
            break
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------