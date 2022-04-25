def split(word):
    return [int(char) for char in word]

def solve(N, X):
    print(sum(split(X)))

def main():
    N = int(input())
    X = input()
    solve(N, X)

if __name__ == "__main__":
    main()

