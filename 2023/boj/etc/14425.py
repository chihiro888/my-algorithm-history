n, m = map(int, input().split())
set_n = set()
answer = 0
for _ in range(n):
    set_n.add(input())
for _ in range(m):
    if input() in set_n:
        answer += 1
print(answer)
