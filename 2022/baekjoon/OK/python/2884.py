import datetime

input = list(map(int, input().split()))

h = input[0]
m = input[1]

solve = (datetime.datetime(2022, 3, 28, h ,m, 0) - datetime.timedelta(minutes=45)).strftime("%-H %-M")

print(solve)