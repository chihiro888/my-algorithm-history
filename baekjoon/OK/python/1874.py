import sys
from collections import deque 


def print_solve(ng, solve):
    if ng:
        print('NO')
    else:
        for s in solve:
            print(s)


def get_solve(d):
    q = deque([])
    solve = []
    ng = False

    curr = 1
    for i in d:
        while True:
            if i > curr-1:
                q.append(curr)
                curr += 1
                solve.append('+')
            elif i <= curr-1:
                x = q.pop()
                solve.append('-')
                if i < x:
                    ng = True
                break

    return ng, solve


def main():
    n = int(input())
    d = []
    for _ in range(n):
        d.append(int(input()))

    ng, solve = get_solve(d)
    print_solve(ng, solve)


if __name__ == "__main__":
    main()