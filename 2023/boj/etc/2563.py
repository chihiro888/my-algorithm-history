import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def debug(d):
    for x in d:
        for y in x:
            print(y, end='')
        print()

def print_array_sum(arr):
    total_sum = 0
    for row in arr:
        for num in row:
            total_sum += num
    print(total_sum)
# -------------------------------


# Please write the code below ---
def main():
    size = int(ip())
    d = [[0] * 100 for _ in range(100)]

    for _ in range(size):
        x, y = mv(int)
        for xi in range(x, x+10):
            for yi in range(y, y+10):
                d[xi][yi] = 1
            
    print_array_sum(d)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------