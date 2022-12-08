n, a = map(int, input().split())

cnt = 0
d = a
while d <= n:
    cnt += n // d
    d *= a
print(cnt)