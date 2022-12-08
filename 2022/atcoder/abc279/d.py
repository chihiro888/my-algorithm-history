import math
import sys


def print_format(x):
    print('{:.10f}'.format(x))


def get_time(a, b, n):
    return round((b * n) + (a/math.sqrt(n+1)), 10)


def main():
    a, b = map(int, sys.stdin.readline().strip().split())

    idx = 0
    while True:
        prev = get_time(a, b, idx)
        curr = get_time(a, b, idx+1)
        if prev < curr:
            print_format(prev)
            break
        idx += 1


if __name__ == "__main__":
    main()
