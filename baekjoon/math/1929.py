def getPrimes():
    n = 1000000
    a = [False,False] + [True]*(n-1)
    primes = []

    for i in range(2, n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return primes
    
def main():
    M, N = map(int, input().split())
    
    primes = getPrimes()
    for prime in primes:
        if M <= prime <= N:
            print(prime) 

if __name__ == '__main__':
    main()
