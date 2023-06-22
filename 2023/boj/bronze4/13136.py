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
    a, b, c = mv(int)
    
    if a % c == 0:
        x = a // c
    else:
        x = (a // c) + 1

    if b % c == 0:
        y = b // c
    else:
        y = (b // c) + 1

    print(x * y)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------