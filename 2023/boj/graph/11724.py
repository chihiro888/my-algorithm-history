import sys
sys.setrecursionlimit(10000)

# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def dfs(g, v, i):
    v[i] = 1
    for e in g[i]:
        if v[e] == 0:
            dfs(g, v, e)
# -------------------------------


# Please write the code below ---
def main():
    n, m = mv(int)

    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = mv(int)
        g[a].append(b)
        g[b].append(a)

    v = [0] * (n+1)
    
    count = 0
    for i in range(1, n+1):
        if v[i] == 0:
            dfs(g, v, i)
            count += 1

    print(count)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------