import sys

n = int(sys.stdin.readline().strip())

queryList = []
for _ in range(n):
    queryList.append(sys.stdin.readline().strip())
    
deque = []
for query in queryList:
    if query.find('push_front') != -1:
        deque.insert(0, query.split(' ')[1])
    elif query.find('push_back') != -1:
        deque.append(query.split(' ')[1])
    elif query.find('pop_front') != -1:
        if len(deque) == 0:
            print(-1)
        else:
            x = deque.pop(0)
            print(x)
    elif query.find('pop_back') != -1:
        if len(deque) == 0:
            print(-1)
        else:
            x = deque.pop()
            print(x)
    elif query.find('size') != -1:
        print(len(deque))
    elif query.find('empty') != -1:
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif query.find('front') != -1:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif query.find('back') != -1:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])