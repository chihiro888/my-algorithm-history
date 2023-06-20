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
    x = lmv(int)
    x = sorted(x)
    a = x[0]
    b = x[1]
    c = x[2]
    if a + b > c:
        print(a + b + c)
    else:
        print((a + b) * 2 - 1)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------