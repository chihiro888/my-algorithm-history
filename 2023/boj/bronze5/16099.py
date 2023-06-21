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
        lt, wt, le, we = mv(int)
        if lt * wt > le * we:
            print('TelecomParisTech')
        elif lt * wt == le * we:
            print('Tie')
        else:
            print('Eurecom')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------