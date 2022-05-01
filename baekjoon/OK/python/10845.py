import sys

n = int(sys.stdin.readline().strip())

queryList = []
for _ in range(n):
    queryList.append(sys.stdin.readline().strip())
    
queue = []
for query in queryList:
    if query.find('push') != -1:
        queue.append(query.split(' ')[1])
    elif query.find('front') != -1:
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[0])
    elif query.find('back') != -1:
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[-1])
    elif query.find('size') != -1:
        print(len(queue))
    elif query.find('empty') != -1:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif query.find('pop') != -1:
        if len(queue) == 0:
            print('-1')
        else:
            x = queue.pop(0)
            print(x)