import sys
from itertools import combinations

# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def get_subsequences(sequence):
    if not sequence:
        return [[]]  # 빈 시퀀스의 부분수열은 빈 시퀀스입니다.

    x = sequence[0]
    subsequences = get_subsequences(sequence[1:])
    new_subsequences = [subseq + [x] for subseq in subsequences]
    return subsequences + new_subsequences

def MEX(X):
    m = 0
    while True:
        if m not in X:
            return m
        m += 1
# -------------------------------


# Please write the code below ---
def main():
    n, k = mv(int)
    a = lmv(int)

    d = get_subsequences(a)
    filtered_list = list(filter(lambda x: len(x) == k, d))

    s = 0
    for f in filtered_list:
        s = max(s, MEX(f))

    print(s)

# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------