def factorial(N):
    if N == 0:
        return 1
    else:
        return N * factorial(N-1)
        
def main():
    N = int(input())
    print(factorial(N))

if __name__ == "__main__":
    main()