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
    a, b = mv(int)
    s = [i for i in range(1, a+1)]
    for _ in range(b):
        start_index, end_index = mv(int)
        subset = s[start_index-1:end_index]
        subset.reverse()
        s[start_index-1:end_index] = subset

    print(' '.join(map(str, s)))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------