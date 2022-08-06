import collections

x = list(map(int, input().split()))
counter = collections.Counter(x)
t = list(counter.values())
if len(t) == 2 and (t[0] == 3 and t[1] == 2) or (t[0] == 2 and t[1] == 3):
    print('Yes')
else:
    print('No')
