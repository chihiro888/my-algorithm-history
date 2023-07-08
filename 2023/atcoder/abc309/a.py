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

    if a == 3 and b == 4:
        print('No')
        exit(0)
    elif a == 6 and b == 7:
        print('No')
        exit(0)

    if b-a == 1:
        print('Yes')
    else:
        print('No')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------