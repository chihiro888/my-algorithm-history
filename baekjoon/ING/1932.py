n = int(input())

d = []
for _ in range(n):
    d.append(list(map(int, input().split())))

memo = [[0, 0] for _ in range(n)]
memo[0] = [0, d[0][0]]

for i in range(1, n):
    print(f'i = {i}')
    print(f'd[i] = {d[i]}')
    print(d[i][0])

    val = max(d[i][memo[i-1][0]], d[i][memo[i-1][0]+1])
    sum = memo[i-1][1] + val
    idx = d[i].index(val)
    memo[i] = [idx, sum]
    print(f'memo = {memo}')