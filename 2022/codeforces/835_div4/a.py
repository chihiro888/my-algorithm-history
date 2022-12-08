n = int(input())
for _ in range(n):
    d = list(map(int, input().split()))
    for x in d:
        if x not in [max(d), min(d)]:
            print(x)
    