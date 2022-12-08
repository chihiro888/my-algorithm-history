n = int(input())
d = list(map(int, input().split()))

# print(f'n = {n}')
# print(f'd = {d}')

print(d[0], end=' ')

for idx in range(1, len(d)):
    print(d[idx] - d[idx-1], end=' ')