x = [10, 20, 10]

sum_a = 0
sum_b = 0
isLeft = True
isRight = False
solve = 0
idx = 0
for i in range(len(x)//2):
    try:
        print('i = ', i)
            
        if isLeft:
            print('left')
            sum_a += x[i]
            isLeft = False
            isRight = True
            idx += 1
        print('sum_a = ', sum_a)
        print('sum_b = ', sum_b)
        print('--------------------------')
        if sum_a == sum_b:
            solve = idx
            
        if isRight:
            print('right')
            sum_b += x[-(i+1)]
            isLeft = True
            isRight = False
            idx += 1
        print('sum_a = ', sum_a)
        print('sum_b = ', sum_b)
        print('--------------------------')
        if sum_a == sum_b:
            solve = idx
    except BaseException:
        break
        
print('solve -> ', solve)