for _ in range(int(input())):
    h, w, n = map(int, input().split())
    print(f'{(h if n % h == 0 else n % h) * 100 + (n // h if n % h == 0 else 1+n // h)}')