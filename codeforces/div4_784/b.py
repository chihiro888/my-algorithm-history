import collections
 
t = int(input())
 
for _ in range(t):
    n = input()
    a = list(map(int, input().split()))
    counter=collections.Counter(a)
    v = counter.values()
    k = counter.keys()
    lv = list(v)
    lk = list(k)
    x = max(lv)
    if x < 3:
        print(-1)
    else:
        cnt = lv.count(x)
        m = 0
        for idx in range(cnt):
            i = lv.index(x, idx)
            d = lk[i]
            if m < d:
                m = d
        print(m)