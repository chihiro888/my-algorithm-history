import sys
from collections import deque 


def solve(d):
    d.pop()
    for x in d:
        # print(f'x = {x}')

        q = deque([])
        s = True
        for i in x:
            if i in ['[', '(']:
                q.append(i)
            elif i in [']']:
                if len(q) == 0:
                    s = False
                    break
                qq = q.pop()
                if qq != '[':
                    s = False
                    break
            elif i in [')']:
                if len(q) == 0:
                    s = False
                    break
                qq = q.pop()
                if qq != '(':
                    s = False
                    break

        if s and len(q) == 0:
            print('yes')
        else:
            print('no')



def main():
    lines = sys.stdin.readlines()
    d = []
    for line in lines:
        t = []
        for x in line.replace('\n', ''):
            if x in ['[', ']', '(', ')']:
                t.append(x)
        d.append(t)
        
    solve(d)


if __name__ == "__main__":
    main()