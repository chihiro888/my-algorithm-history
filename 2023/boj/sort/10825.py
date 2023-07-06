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
    for _ in range(size):
        x = lmv(str)
        for i in range(1, 4):
            x[i] = int(x[i])
        d.append(x)
    
    d.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

    for x in d:
        print(x[0])
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------