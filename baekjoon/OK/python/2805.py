n, m = map(int, input().split())

d = list(map(int, input().split()))

start = 1
end = max(d)

while start <= end:
    mid = (start+end) // 2
    
    t = 0
    for i in d:
        if i >= mid:
            t += i - mid
    
    if t >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)