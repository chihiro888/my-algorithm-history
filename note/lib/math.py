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
def gcd(a:int, b:int):  
    while b > 0:
        a, b = b, a % b
    return a


# 최소공배수
def lcm(a:int, b:int):
    return a * b / gcd(a, b)


# 에라토스테네스의 체 - 소수 리스트
# n 미만까지 구하기 때문에 이하로 구하기 위해서 n+1 을 넣을 것
def prime_list(n:int):
    s = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if s[i] == True:
            for j in range(i+i, n, i):
                s[j] = False
    return [i for i in range(2, n) if s[i] == True]