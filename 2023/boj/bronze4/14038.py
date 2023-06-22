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
    d = [ip() for _ in range(6)]
    x = d.count('W')
    if x in [5, 6]:
        print('1')
    elif x in [3, 4]:
        print('2')
    elif x in [1, 2]:
        print('3')
    else:
        print('-1')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------