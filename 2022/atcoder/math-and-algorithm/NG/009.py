# 1 <= n <= 60
# 1 <= s <= 10000
n, s = map(int, input().split())
# 1 <= a[i] <= 10000
a = list(map(int, input().split()))

solve = False
for i in range(0, len(a)):
    if a[i] == s:
        solve = True
    for j in range(i+1, len(a)):
        if a[i] + a[j] == s:
            solve = True
        for k in range(j+1, len(a)):
            if a[i] + a[j] + a[k] == s:
                solve = True
            for l in range(k+1, len(a)):
                if a[i] + a[j] + a[k] + a[l] == s:
                    solve = True
                for m in range(l+1, len(a)):
                    if a[i] + a[j] + a[k] + a[l] + a[m] == s:
                        solve = True
                    for n in range(m+1, len(a)):
                        if a[i] + a[j] + a[k] + a[l] + a[m] + a[n] == s:
                            solve = True
                        if solve: break
                    if solve: break
                if solve: break
            if solve: break
        if solve: break
    if solve: break
        
if solve:
    print('Yes')
else:
    print('No')