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
    s = ip()
    i = int(ip())

    print(s[i-1])
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------