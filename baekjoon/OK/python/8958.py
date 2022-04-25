def split(word):
    return [char for char in word]

N = int(input())
I = []
for n in range(0, N):
    I.append(input())
    
for i in I:
    scoreSum = 0
    score = 0
    for x in split(i):
        if x == 'O':
            score += 1
            scoreSum += score
        if x == 'X':
            score = 0
    print(scoreSum)