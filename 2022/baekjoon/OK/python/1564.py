n = int(input())
d = 1
for i in range(2,n+1):
    d *= i
    while True:
        if str(d)[-1] == "0":
            d //= 10
        else:
            break
    d %= 1000000000000
print(str(d)[-5:])