import math

d = math.factorial(int(input()))

x = [x for x in str(d)]

cnt = 0
for idx in range(len(x)-1, 0, -1):
    if x[idx] == '0':
        cnt += 1
    else:
        break

print(f'{cnt}')
