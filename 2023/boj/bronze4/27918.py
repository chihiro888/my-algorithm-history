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
    d = []
    sd = 0
    sp = 0
    for _ in range(size):
        x = ip()
        if x == 'D':
            sd += 1
        elif x == 'P':
            sp += 1
        d.append(x)
        if abs(sd-sp) == 2:
            break
    print(f'{sd}:{sp}')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------