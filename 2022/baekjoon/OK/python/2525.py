import datetime

I = list(map(int, input().split()))
C = int(input())

A = I[0]
B = I[1]

solve = (datetime.datetime(2022, 3, 28, A ,B, 0) + datetime.timedelta(minutes=C)).strftime("%-H %-M")

print(solve)