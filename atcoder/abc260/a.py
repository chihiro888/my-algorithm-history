import collections
s = input()
sList = [x for x in s]
x = {}
x = collections.Counter(sList)
x_keys = list(x.keys())
x_values = list(x.values())

try:
    print(x_keys[x_values.index(1)])
except BaseException:
    print(-1)
