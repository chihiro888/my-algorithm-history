t = int(input())

for _ in range(t):
    rating = int(input())
    
    if rating <= 1399:
        print('Division 4')
    elif 1400 <= rating <= 1599:
        print('Division 3')
    elif 1600 <= rating <= 1899:
        print('Division 2')
    else:
        print('Division 1')