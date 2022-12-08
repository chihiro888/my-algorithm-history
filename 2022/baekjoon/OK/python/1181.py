import sys


def word_sort(d):
    d = set(d)
    d = sorted(d, key=lambda x : (len(x), x))
    for x in d:
        print(x)

def main():
    n = int(sys.stdin.readline().strip())
    d = []
    for _ in range(n):
        d.append(sys.stdin.readline().strip())
    word_sort(d)    

if __name__ == "__main__":
    main()