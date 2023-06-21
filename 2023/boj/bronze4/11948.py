import sys
from itertools import combinations

# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def get_max_combination(lst, n, m):
    combinations_lst = list(combinations(lst, m))
    max_value = max(sum(combination) for combination in combinations_lst)
    return max_value
# -------------------------------


# Please write the code below ---
def main():
    a = int(ip())
    b = int(ip())
    c = int(ip())
    d = int(ip())
    e = int(ip())
    f = int(ip())

    x = [a, b, c, d]
    y = [e, f]

    print(get_max_combination(x, len(x), 3) + get_max_combination(y, len(y), 1))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------