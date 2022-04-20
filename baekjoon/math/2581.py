def getPrimes():
    n = 10000
    a = [False,False] + [True]*(n-1)
    primes = []

    for i in range(2, n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return primes
    
def main():
    M = int(input())
    N = int(input())
    
    primes = getPrimes()
    sum = 0
    minPrime = 0
    for prime in primes:
        if M <= prime <= N:
            if sum == 0:
                minPrime = prime
            sum += prime 
    
    if sum == 0:
        print(-1)
    else:
        print(sum)
        print(minPrime)
        
if __name__ == '__main__':
    main()
