# 소인수분해
def factorization(x:int):
    d = 2
    while d <= x:
        if x % d == 0:
            print(d)
            x = x / d
        else:
            d = d + 1
