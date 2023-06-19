import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def find_largest_number(array):
    max_num = float('-inf')
    max_index = None

    for i, row in enumerate(array):
        for j, num in enumerate(row):
            if num > max_num:
                max_num = num
                max_index = (i+1, j+1)

    return max_num, max_index

def print_list(l: list):
    print(' '.join(map(str, l)))
# -------------------------------


# Please write the code below ---
def main():
    d = []
    for _ in range(9):
        d.append(lmv(int))
    a, b = find_largest_number(d)
    print(a)
    print_list(b)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------