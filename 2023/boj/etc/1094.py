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
    d = int(ip())
    x = [ 64, 32, 16, 8, 4, 2, 1 ]
    s = []
    for i in x:
        if d >= i and sum(s) + i <= d:
            s.append(i)
    print(len(s))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------