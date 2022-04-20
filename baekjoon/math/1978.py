def getPrimes():
    n = 1000
    a = [False,False] + [True]*(n-1)
    primes = []

    for i in range(2, n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return primes
    
def main():
    N = int(input())
    dataList = list(map(int, input().split()))
    primes = getPrimes()
    
    solve = 0
    for data in dataList:
        solve += primes.count(data)
    
    print(solve)
    
if __name__ == '__main__':
    main()
