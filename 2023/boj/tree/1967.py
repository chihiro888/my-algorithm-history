import sys
sys.setrecursionlimit(10**9)


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def dfs(g, d, x, wei):
    for i in g[x]:
        a, b = i
        if d[a] == -1:
            d[a] = wei + b
            dfs(g, d, a, wei + b)
# -------------------------------


# Please write the code below ---
def main():
    size = int(ip())
    g = [[] for _ in range(size + 1)]

    for _ in range(size - 1):
        a, b, c = mv(int)
        g[a].append([b, c])
        g[b].append([a, c])

    d = [-1] * (size + 1)
    d[1] = 0
    dfs(g, d, 1, 0)

    s = d.index(max(d))
    d = [-1] * (size + 1)
    d[s] = 0
    dfs(g, d, s, 0)

    print(max(d))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------