def shift(d):
    nd = [0] * len(d)
    for i in range(len(d)):
        nd[i-1] = d[i]
    nd[-1] = 0
    
    return nd

def main():
    n, k = list(map(int, input().split()))

    d = list(map(int, input().split()))

    for _ in range(k):
        d = shift(d)

    for x in d:
        print(x, end=' ')

if __name__ == "__main__":
    main()