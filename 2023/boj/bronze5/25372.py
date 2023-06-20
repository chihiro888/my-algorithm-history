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
    size = int(ip())
    for _ in range(size):
        s = ip()
        if 6 <= len(s) and len(s) <= 9:
            print('yes')
        else:
            print('no')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------