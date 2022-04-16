import collections
 
def solve(D):
    c = collections.Counter(D)
    idx = 0
    max = 0
    savedIdx = 0
    for n in list(c.values()):
        if max < n:
            max = n
            savedIdx = idx
        idx += 1
    if list(c.values()).count(max) > 1:
        print('?')
    else:
        print(list(c.keys())[savedIdx].upper())

def main():
    D = input().lower()
    solve(D)
    
if __name__ == "__main__":
    main()