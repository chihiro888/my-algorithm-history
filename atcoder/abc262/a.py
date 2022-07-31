y = int(input())

# print(y%4)

if y%4 == 2:
    print(y)
elif y%4 == 3:
    print(y+3)
elif y%4 == 0:
    print(y+2)
elif y%4 == 1:
    print(y+1)

# 2022 -> 505.5 -> 2 -> +0
# 2023 -> 505.75 -> 3 -> +3
# 3000 -> 750.0 -> 0 -> +2