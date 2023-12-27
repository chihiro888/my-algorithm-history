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
d = []
for i in range(1, 50):
    for _ in range(i):
        d.append(i)

s, e = mv(int)
print(sum(d[s-1:e]))
# -------------------------------