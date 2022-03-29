import collections

I = list(map(int, input().split()))
c = collections.Counter(I)

if 3 in c.values():
    match = list(c.keys())[0]
    print(10000+(match*1000))
elif 2 in c.values():
    idx = 0
    for n in list(c.values()):
        if n == 2:
            match = list(c.keys())[idx]
            print(1000+match*100)
            break
        idx += 1
else:
    I.sort(reverse=True)
    max = I[0]
    print(max*100)