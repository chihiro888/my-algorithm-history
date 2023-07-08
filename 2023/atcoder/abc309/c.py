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
    n, k = mv(int)
    x = []
    for _ in range(n):
        d, p = mv(int)
        x.append([d, p])

    x = sorted(sorted(x, key=lambda x: x[1]), key=lambda x: x[0])
    total = sum([x[i][1] for i in range(n)])
    
    if total <= k:
        print(1)
    else:
        for i in range(n):
            e = x[i]
            total -= e[1]
            if k >= total:
                print(e[0] + 1)
                break
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------