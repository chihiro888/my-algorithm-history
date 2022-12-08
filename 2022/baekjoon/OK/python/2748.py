def fib(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

def main():
    n = int(input())
    print(fib(n))

if __name__ == "__main__":
    main()