def split(word):
    return [int(char) for char in word]
    
def SN(n):
    x = split(str(n))
    return n + sum(x)

def solve():
    store = [0] * 10000

    for n in range(1, 10000):
        if store[n] != 0:
            pass
        else:
            store[n] = SN(n)
        
        if n not in store:
            print(n)

solve()