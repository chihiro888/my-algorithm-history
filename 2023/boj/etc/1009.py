import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
d = [
    [10],
    [1],
    [2, 4, 8, 6],
    [3, 9, 7, 1],
    [4, 6],
    [5],
    [6],
    [7, 9, 3, 1],
    [8, 4, 2, 6],
    [9, 1]
]

def solve(a, b):
    if len(str(a)) > 1:
        if int(str(a)[-2] + str(a)[-1]) == 10:
            print(10)
            return False
    last_number = int(str(a)[-1])
    rule_size = len(d[last_number])
    i = b % rule_size
    print(d[last_number][i-1])

# -------------------------------


# Please write the code below ---
t = int(ip())
for i in range(t):
    a, b = mv(int)
    solve(a, b)
# -------------------------------
