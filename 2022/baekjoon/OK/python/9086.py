n = int(input())
d = []
for _ in range(n):
    d.append(input())

for i in d:
    print(f'{i[0]}{i[-1]}')