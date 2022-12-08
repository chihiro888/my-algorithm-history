from collections import deque

# 1 <= n <= 500000
n = int(input())

d = deque()
for i in range(1, n+1):
    d.append(i)

while len(d) > 1:
    d.popleft()
    d.append(d.popleft())
print(d[0])