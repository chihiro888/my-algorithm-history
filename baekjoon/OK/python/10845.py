import sys
from collections import deque


q = deque([])


def op(d):
    if d.find('push') != -1:
        d = d.split(' ')
        value = d[1]
        q.append(value)
        return False
    
    if d.find('pop') != -1:
        if len(q) == 0:
            print(-1)
        else:
            x  = q.popleft()
            print(x)
        return False
        
    if d.find('front') != -1:
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
        return False
        
    if d.find('back') != -1:
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
        return False
    
    if d.find('size') != -1:
        print(len(q))
        return False
    
    if d.find('empty') != -1:
        if len(q) == 0:
            print(1)
        else:
            print(0)
        return False
    
    
def main():
    n = int(sys.stdin.readline().strip())

    for _ in range(n):
        d = sys.stdin.readline().strip()
        op(d)


if __name__ == "__main__":
    main()