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
    x = lmv(int)
    x.sort(reverse=True)

    if len(x) > 1:
        print(x[k-1])
    else:
        print(x[0])
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------