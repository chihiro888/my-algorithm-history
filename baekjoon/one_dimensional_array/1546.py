import statistics

N = int(input())
I = list(map(int, input().split()))
M = max(I)

result = []
for i in I:
    result.append(i/M*100)
    
print(statistics.mean(result))