import sys
from collections import deque

def josephus_permutation(n, k):
    d = [n for n in range(1, n+1)]
    solve = []
    idx = 0
    while True:
        idx -= 1
        idx = (idx + k) % len(d)
        solve.append(d.pop(idx))
        if len(d) == 0:
            break
    
    return solve


def main():
    n, k = map(int, sys.stdin.readline().strip().split())
    
    d = josephus_permutation(n, k)
    
    print(f"<{', '.join([str(x) for x in d])}>")

if __name__ == "__main__":
    main()