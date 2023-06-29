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
    n = int(ip())
    for i in range(1, 1000):
        if n < i * i:
            print(f'The largest square has side length {i-1}.')
            break
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------