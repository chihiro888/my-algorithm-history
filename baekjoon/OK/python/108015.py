import bisect
import sys

def main():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    m = int(sys.stdin.readline().strip())
    b = list(map(int, sys.stdin.readline().strip().split()))

    a = sorted(a)

    for i in b:
        if bisect.bisect_right(a, i) - bisect.bisect_left(a, i) > 0:
            print('1', end=' ')
        else:
            print('0', end=' ')
        
        # print(bisect.bisect_right(a, i) - bisect.bisect_left(a, i), end=' ')

if __name__ == "__main__":
    main()