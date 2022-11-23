n = int(input())

x = n 
for i in range(1, n+1):
    print(f"{' ' * (x-1)}{'*' * ((i*2)-1)}")
    x -= 1