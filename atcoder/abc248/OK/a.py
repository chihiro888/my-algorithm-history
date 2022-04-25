def split(word):
    return [int(char) for char in word]

s = input()
data = split(s)

for n in range(0, 10):
    if n not in data:
        print(n)
        
'''
https://atcoder.jp/contests/abc248/submissions/31008547
'''