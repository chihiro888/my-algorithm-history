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
    d = lmv(int)
    s = [0] * d[0]
    for _ in range(d[1]):
        x = lmv(int)
        for idx in range(x[0]-1, x[1]):
            s[idx] = x[2]

    print(' '.join(map(str, s)))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------