x, y = map(int, input().split())

z = (y * 100) // x

start = 1
end = x

if z >= 99:
    print(-1)
else:
    while start <= end:

        mid = (start + end) // 2

        s = (y + mid) * 100 // (x + mid) 

        if s <= z:
            start = mid + 1
        else:
            end  = mid - 1

    print(end + 1)