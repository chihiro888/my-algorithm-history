n = int(input())
sum = 0
for _ in range(n):
    d = input()
    x = int(d[2: len(d)])
    if x <= 90:
       sum += 1

print(sum) 