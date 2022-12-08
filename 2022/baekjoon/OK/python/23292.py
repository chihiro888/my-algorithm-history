import sys

def solve(b, d):
    b = [int(x) for x in b]
    xList = []
    for i in d:
        i = [int(x) for x in i]
        
        r = (((b[0]-i[0]) ** 2) + ((b[1]-i[1]) ** 2) + ((b[2]-i[2]) ** 2) + ((b[3]-i[3]) ** 2)) * \
            (((b[4]-i[4]) ** 2) + ((b[5]-i[5]) ** 2)) * \
            (((b[6]-i[6]) ** 2) + ((b[7]-i[7]) ** 2))
            
        xList.append([''.join([str(x) for x in i]), r])
            
    k = sorted(xList, key = lambda x : (-x[1], x[0]))
    
    print(f'{k[0][0]}')


def main():
    b = sys.stdin.readline().strip()
    t = int(sys.stdin.readline().strip())
    d = []
    for _ in range(t):
        d.append(sys.stdin.readline().strip())
        
    solve(b, d)


if __name__ == "__main__":
    main()