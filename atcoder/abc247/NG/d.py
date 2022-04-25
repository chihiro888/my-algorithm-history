# FAIL / AC x 1 / WA x 1 / TLE x 20

Q = int(input())
 
task = []
 
for n in range(Q):
    query = list(map(int, input().split()))
    
    # get command
    command = query[0]
    
    if command == 1:
        # back push
        count = query[2]
        data = query[1]
        
        # proccess
        for _ in range(count):
            task.append(data)

    elif command == 2:
        # front pop
        count = query[1]
        
        # for print
        sum = 0
        
        # process
        # but, N(1000000000) issue
        for _ in range(count):
            p = task.pop(0)
            sum += p
        
        # solve
        print('sum -> ', sum)
        
'''
https://atcoder.jp/contests/abc247/submissions/30885779
'''