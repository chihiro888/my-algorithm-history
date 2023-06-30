import sys
sys.setrecursionlimit(10**6)

# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
# 이차원 배열 디버깅
def print_arr(arr):
    for y in arr:
        for x in y:
            print(x, end='')
        print()
    print('----------------')


# 문자열을 리스트로 변환
def str_to_list(s:str):
    return [int(x) for x in s]

# 이차원 배열에서 요소 찾아서 인덱스 반환
def find_negative_one(arr):
    for i, row in enumerate(arr):
        for j, element in enumerate(row):
            if element == 1:
                return i, j
    return -1, -1

# 2차원 배열을 1차원 배열로 변경
def flatten_2d_array(arr):
    return [element for sublist in arr for element in sublist]

# DFS 탐색
def dfs(g, m, n, num):
    g[n][m] = num

    # 위
    if n > 0 and g[n-1][m] == 1:
        dfs(g, m, n-1, num)
    # 아래
    if n < len(g) - 1 and g[n+1][m] == 1:
        dfs(g, m, n+1, num)
    # 왼쪽
    if m > 0 and g[n][m-1] == 1:
        dfs(g, m-1, n, num)
    # 오른쪽
    if m < len(g[0]) - 1 and g[n][m+1] == 1:
        dfs(g, m+1, n, num)
# -------------------------------


# Please write the code below ---
def main():
    # 입력
    size = int(ip())
    g = []
    for _ in range(size):
        g.append(str_to_list(ip()))

    # DFS로 단지 수 매핑
    num = -1
    while True:
        n, m = find_negative_one(g)

        if n == -1 and m == -1:
            break

        dfs(g, m, n, num)

        num -= 1

    # 2차원 배열을 1차원 배열로 변경
    arr = flatten_2d_array(g)

    # 총 단지수
    x = abs(min(arr))

    # 정답출력
    print(x)

    # 단지내 집의 수
    d = []
    for i in range(1, x+1):
        d.append(arr.count(i * -1))

    # 단지내 집의 수 오름차순 정렬
    d.sort()

    # 정답출력
    for x in d:
        print(x)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------