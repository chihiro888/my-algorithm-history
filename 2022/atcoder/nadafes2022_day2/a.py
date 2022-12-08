# 1 <= n <= 1000000000
n = int(input())

# 1 <= k <= m <= 1000000000
k, m = map(int, input().split())

# print(f'n = {n}')
# print(f'k = {k}, m = {m}')

a = []
b = []
for i in range(0, n):
    a.append(i)
    b.append((i+k) % m)

# print(f'a = {a}')
# print(f'b = {b}')

a.sort()
b.sort()

# print(f'sorted a = {a}')
# print(f'sorted b = {b}')

diff = list(set(b) - set(a))

# print('diff -> ', diff)

if len(diff) == 0:
    print('Yes')
else:
    print('No')