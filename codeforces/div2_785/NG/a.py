import copy

# score table
score = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
}

def changeTurn(alice, bob):
    if alice:
        alice = False
        bob = True
    elif bob:
        alice = True
        bob = False
    return alice, bob

def solve(s):
    # string list
    sList = [char for char in s]
    # sList.sort()

    # init
    aliceScore = 0
    bobScore = 0
    alice = True
    bob = False

    # solve
    while(len(sList) != 0):
        if alice:
            # alice turn
            if len(sList) % 2 == 0:
                # even case
                a = copy.deepcopy(sList)
                b = copy.deepcopy(sList)
                b.reverse()
                x = 0
                y = 0
                xPopCnt = 0
                yPopCnt = 0
                for n in range(len(sList)):
                    x += score[a.pop()]
                    xPopCnt += 1
                for n in range(len(sList)):
                    y += score[b.pop()]
                    yPopCnt += 1
                    
                if x > y:
                    sList = a
                    aliceScore = x
                else:
                    sList = b
                    aliceScore = y
                    
                alice, bob = changeTurn(alice, bob)
            else:
                # odd case
                a = copy.deepcopy(sList)
                b = copy.deepcopy(sList)
                b.reverse()
                x = 0
                y = 0
                xPopCnt = 0
                yPopCnt = 0
                for n in range(len(sList) -1):
                    x += score[a.pop()]
                    xPopCnt += 1
                for n in range(len(sList) -1):
                    y += score[b.pop()]
                    yPopCnt += 1
                    
                if x > y:
                    sList = a
                    aliceScore = x
                else:
                    sList = b
                    aliceScore = y
                    
                alice, bob = changeTurn(alice, bob)
        elif bob:
            # bob turn
            if len(sList) % 2 == 0:
                # even case
                a = copy.deepcopy(sList)
                b = copy.deepcopy(sList)
                b.reverse()
                x = 0
                y = 0
                xPopCnt = 0
                yPopCnt = 0
                for n in range(len(sList) -1):
                    x += score[a.pop()]
                    xPopCnt += 1
                for n in range(len(sList) -1):
                    y += score[b.pop()]
                    yPopCnt += 1
                    
                if x > y:
                    sList = a
                    bobScore = x
                else:
                    sList = b
                    bobScore = y
                    
                alice, bob = changeTurn(alice, bob)
            else:
                # odd case
                a = copy.deepcopy(sList)
                b = copy.deepcopy(sList)
                b.reverse()
                x = 0
                y = 0
                xPopCnt = 0
                yPopCnt = 0
                for n in range(len(sList)):
                    x += score[a.pop()]
                    xPopCnt += 1
                for n in range(len(sList)):
                    y += score[b.pop()]
                    yPopCnt += 1

                if x > y:
                    sList = a
                    bobScore = x
                else:
                    sList = b
                    bobScore = y
                    
                alice, bob = changeTurn(alice, bob)
                break

    if aliceScore > bobScore:
        print(f'Alice {aliceScore-bobScore}')
    else:
        print(f'Bob {bobScore-aliceScore}')
            
def main():
    # 1 <= t <= 50000
    t = int(input())
    for _ in range(t):
        # 1 <= s <= 200000
        s = input()
        solve(s)
        
if __name__ == '__main__':
    main()