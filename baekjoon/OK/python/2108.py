import sys
from collections import Counter

n = int(sys.stdin.readline())

d = []
for i in range(n):
    d.append(int(sys.stdin.readline()))

d.sort()
dc = Counter(d).most_common()

# 산술평균
print(round(sum(d) / n))

# 중앙값
print(d[n // 2])

# 최빈값
if len(dc) > 1:
    if dc[0][1] == dc[1][1]:
        print(dc[1][0])
    else:
        print(dc[0][0])
else:
    print(dc[0][0])

# 범위
print(d[-1] - d[0])