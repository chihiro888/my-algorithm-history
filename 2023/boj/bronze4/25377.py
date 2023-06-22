n = int(input())
stores = []
for _ in range(n):
    a, b = map(int, input().split())
    stores.append((a, b))

time = [b for a, b in stores if b >= a]

if time:
    print(min(time))
else:
    print(-1)