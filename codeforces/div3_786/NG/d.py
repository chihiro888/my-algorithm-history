'''
<surrend>
If b currently has odd length,
you can choose:
place the element from a to the left or to the right of the middle element of b.
'''

# 1 <= n < 200000
n = int(input())
b = []
c = []
for _ in range(n):
    n = int(input())
    a = list(map(int, input().split()))
    print('start a = ', a)
    
    # Step 1
    while(True):
        if len(b) % 2 == 0:
            # length of b is even
            x = a.pop()
            b.insert(len(b) // 2, x)
        else:
            # length of b is odd
            x = a.pop()
            if len(b) == 0:
                b.append(x)
            else:
                # issue
                if b[len(b) // 2] < x:
                    # left insert
                    b.insert(len(b) // 2, x)
                else:
                    # right insert
                    b.insert(len(b) // 2 + 1, x)
        
        # exit condition
        if len(b) == 0: break
            
        print('a = ', a)
        print('b = ', b)
    