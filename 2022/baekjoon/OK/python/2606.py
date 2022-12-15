import sys


# Utilities ---------------------
debug = False
def p(name, value):
    if debug: print(f'{name} = {value}')
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
cnt = 0
# -------------------------------


# Function Block ----------------
def dfs(s, v, g):
    global cnt
    v[s] = 1
    for i in g[s]:
        if v[i] == 0:
            dfs(i, v, g)
            cnt += 1
# -------------------------------


# Please write the code below ---
def main():
    c = int(ip())
    n = int(ip())
    g = [[] * c for _ in range(c+1)]
    v = [0] * (c+1)

    for _ in range(n):
        s, e = mv(int)
        g[s].append(e)
        g[e].append(s)

    dfs(1, v, g)

    print(cnt)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------