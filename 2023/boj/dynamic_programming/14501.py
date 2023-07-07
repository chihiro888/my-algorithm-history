import sys
import itertools


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def get_all_pattern(arr):
    lst = [x for x in range(1, len(arr))]
    result = []
    for r in range(1, len(lst) + 1):
        subsets = itertools.combinations(lst, r)
        result.extend(subsets)
    result = [list(subset) for subset in result]
    return result

def is_valid(t, k):
    check = True
    if len(k) > 1:
        for i in range(0, len(k)-1):
            d = k[i+1] - k[i]
            if t[k[i]] > d:
                check = False
    if t[k[-1]] > len(t) - k[-1]:
        check = False
    return check

def search_pattern(t):
    ss = get_all_pattern(t)
    d = []
    for s in ss:
        if is_valid(t, s):
            d.append(s)
    return d

def get_sum_list(p, d):
    s = []
    for x in d:
        total = 0
        for idx in x:
            total += p[idx]
        s.append(total)
    return s
# -------------------------------


# Please write the code below ---
def main():
    # 입력
    size = int(ip())
    t = [0]
    p = [0]
    for _ in range(size):
        ti, pi = mv(int)   
        t.append(ti)
        p.append(pi)

    # 패턴 찾기
    d = search_pattern(t)

    # price의 합
    s = get_sum_list(p, d)

    if len(s) == 0:
        print(0)
    else:
        print(max(s))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------