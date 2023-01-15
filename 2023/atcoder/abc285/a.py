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
    t = [[], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [], [], [], [], [], [], [], []]
    a, b = mv(int)
    x = t[a]
    if b in x:
        print('Yes')
    else:
        print('No')

# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------