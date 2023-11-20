import sys
from itertools import combinations

# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def find_combination(lst):
    # 2개 요소를 제외한 모든 가능한 조합 찾기
    for r in range(len(lst) - 1, 1, -1):  # 2개 요소 제외
        for combo in combinations(lst, r):
            if sum(combo) == 100:
                return combo

    return None
# -------------------------------


# Please write the code below ---
d = []
for _ in range(9):
    d.append(int(ip()))

r = list(find_combination(d))
r.sort()
for x in r:
    print(x)

# -------------------------------