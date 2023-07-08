import sys

# n = 물품의 수
# k = 버틸 수 있는 무게
n, k = map(int, sys.stdin.readline().split()) 
arr = [(0, 0)]
chart = [[0] * (k + 1) for _ in range(n + 1)]
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    arr.append((w, v))

for i in range(1, n + 1): # 물건 하나씩
    for j in range(1, k + 1): # 1 ~ k 무게까지 표 작성
        w = arr[i][0]
        v = arr[i][1]
        if j < w: 
            # 해당 물건이 더 큰 경우, 이전 표값으로 넣기
            chart[i][j] = chart[i - 1][j]
        else: 
            # 해당 물건이 들어가는 사이즈인 경우
            # 이전 값과 비교
            chart[i][j] = max(chart[i - 1][j], v + chart[i - 1][j - w]) 

print(chart[n][k])