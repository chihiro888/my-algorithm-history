A, B, N = map(int, input().split())

for _ in range(N):
    A = (A % B) * 10
    r = A // B
    
print(r)