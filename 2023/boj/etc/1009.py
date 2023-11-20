import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def op(a, b):
    return int(str(a * b)[-1])
    
def solve(a, b):
    q = []
    q.append(op(a, a))
    while q[-1] != a:
        q.append(op(a, q[-1]))
    q.insert(0, q.pop())
    x = b % len(q)
    print(q[x-1])
# -------------------------------


# Please write the code below ---
t = int(ip())
for i in range(t):
    a, b = mv(int)
    solve(a, b)
# -------------------------------
