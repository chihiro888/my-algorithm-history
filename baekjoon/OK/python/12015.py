from bisect import bisect_left
 
 
def LIS(v):
    if len(v) == 0:
        return 0
 
    tail = [0 for i in range(len(v) + 1)]
    length = 1
 
    tail[0] = v[0]
 
    for i in range(1, len(v)):
        if v[i] > tail[length-1]:
            tail[length] = v[i]
            length += 1
 
        else:
            tail[bisect_left(tail, v[i], 0, length-1)] = v[i]
            
    print(length)
    
    while 0 in tail:
        tail.remove(0)
    
    print(' '.join(str(x) for x in tail))
 
 
def main():
    n = int(input())
    d = list(map(int, input().split()))
    LIS(d)


if __name__ == "__main__":
    main()