# 1 <= q <= 10000
q = int(input())
for _ in range(q):
    # a non-empty string s
    # consisting only of Latin letters 'a'
    # The length of s doesn't exceed 50
    s = input()
    # a non-empty string t
    # lowercase Latin letters
    # The length of t doesn't exceed 50
    t = input()
    
    if t == 'a':
        # pattern1, t is only a
        print(1)
    elif t.find('a') != -1:
        # pattern2, 
        print(-1) 
    elif t.count('a') == 0:
        print(2 ** len(s))