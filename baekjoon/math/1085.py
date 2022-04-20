x, y, w, h = map(int, input().split())
d = [x, y, w-x, h-y]
print(min(d))