def split(word):
    return [int(char) for char in word]

def solve(N):
    store = [0] * 1000

    # get 1 ~ 99
    for n in range(1,100):
        store[n] = 9

    # get 100 ~ 999
    for n in range(100, 1000):
        x = split(str(n))
        d = x[1] - x[0]
        if x[2] == x[1] + d:
            store[int(f'{x[0]}{x[1]}{x[2]}')] = 9

    print(store[1:N+1].count(9))

def main():
    N = int(input())
    solve(N)

if __name__ == "__main__":
    main()