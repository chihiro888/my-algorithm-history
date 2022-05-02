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
    
    
'''
In one move,
you can replace any letter 'a' in the string s with a string t.
Note that after the replacement string s might contain letters other than 'a'.

You can perform an arbitrary number of moves (including zero).
How many different strings can you obtain?
Print the number, or report that it is infinitely large.

Two strings are considered different if they have different length,
or they differ at some index.

각 테스트 케이스에 대해 임의의 이동량(0 포함) 후에
얻을 수 있는 다른 문자열의 수를 인쇄합니다.
숫자가 무한히 크면 -1을 인쇄합니다.
그렇지 않으면 번호를 인쇄합니다.

aaaa
a

t is only a -> 1

aa
abc

aa
ab

aa
ac

t include a + i -> -1

a
b

a
bb

a
cbd

t not include a, single word -> 2

aa
cb

aa, acb, cba, cbcb => 2^2

aaa
cb

aaa, aacb, acba, cbaa, cbcba, cbacb, acbcb, cbcbcb => 2^3

'''