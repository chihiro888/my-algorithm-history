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
    a, b, c, d, e, f = mv(int)

    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if (a * x) + (b * y) == c and d * x + e * y == f:
                print(f'{x} {y}')
                break

# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------