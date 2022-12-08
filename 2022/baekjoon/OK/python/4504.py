n = int(input())

while True:
    x = int(input())
    if x == 0:
        break
    
    if x % n == 0:
        print(f'{x} is a multiple of {n}.')
    else:
        print(f'{x} is NOT a multiple of {n}.')