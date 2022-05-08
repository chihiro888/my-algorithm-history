t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # print(f'a before = {a}')
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            if a[i] > 0 and a[j] < 0:
                a[i] *= -1
                a[j] *= -1
    # print(f'a after = {a}')
    
    is_sorted = (sorted(a) == a)
    if is_sorted:
        print('YES')
    else:
        print('NO')