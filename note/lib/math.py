# 소인수분해
def factorization(x:int):
    d = 2
    while d <= x:
        if x % d == 0:
            print(d)
            x = x / d
        else:
            d = d + 1


# 최대공약수
def gcd(a, b):  
    while b > 0:
        a, b = b, a % b
    return a


# 최소공배수
def lcm(a, b):
    return a * b / gcd(a, b)