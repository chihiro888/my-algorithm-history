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
    x = [int(ip()) for _ in range(3)]
    x.sort()
    print(x[1])
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------