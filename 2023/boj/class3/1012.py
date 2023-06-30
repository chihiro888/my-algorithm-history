import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def print_arr(arr):
    for y in arr:
        for x in y:
            print(x, end='')
        print()
    print('----------------')
# -------------------------------


# Please write the code below ---
def main():
    size = int(ip())
    m, n, k = mv(int)
    arr = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = mv(int)
        arr[y][x] = 1
    print_arr(arr)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------