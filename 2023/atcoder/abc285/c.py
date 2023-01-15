import sys
import string

# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def col2num(col):
    num = 0
    for c in col:
        if c in string.ascii_letters:
            num = num * 26 + (ord(c.upper()) - ord('A')) + 1
    return num
# -------------------------------


# Please write the code below ---
def main():
    s = ip()
    print(col2num(s))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------