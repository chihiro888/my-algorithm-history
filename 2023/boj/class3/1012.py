import sys
sys.setrecursionlimit(10**6)

# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def find_negative_one(arr):
    for i, row in enumerate(arr):
        for j, element in enumerate(row):
            if element == 1:
                return i, j
    return -1, -1

def dfs(g, m, n):
    g[n][m] = 9

    # 위
    if n > 0 and g[n-1][m] == 1:
        dfs(g, m, n-1)
    # 아래
    if n < len(g) - 1 and g[n+1][m] == 1:
        dfs(g, m, n+1)
    # 왼쪽
    if m > 0 and g[n][m-1] == 1:
        dfs(g, m-1, n)
    # 오른쪽
    if m < len(g[0]) - 1 and g[n][m+1] == 1:
        dfs(g, m+1, n)

# -------------------------------


# Please write the code below ---
def main():
    size = int(ip())

    for _ in range(size):
        # m은 가로, n은 세로
        m, n, k = mv(int)
        g = [[0] * m for _ in range(n)]

        for _ in range(k):
            # m은 가로, n은 세로
            m, n = mv(int)
            g[n][m] = 1

        count = 0
        while True:
            n, m = find_negative_one(g)

            if n == -1 and m == -1:
                break

            dfs(g, m, n)

            count += 1

        print(count)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------