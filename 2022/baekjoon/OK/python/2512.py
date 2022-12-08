n = int(input())
d = list(map(int, input().split()))
k = int(input())

start = 0
end = max(d)

while start <= end:
    mid = (start + end) // 2

    s = 0
    for x in d:
        if x >= mid:
            s += mid
        else:
            s += x

    if s <= k:
        start = mid + 1
    else:
        end = mid - 1

print(end)
