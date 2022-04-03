import string

def split(word):
    return [char for char in word]
    
def solve(X):
    inputList = split(X)
    arpabet = split(string.ascii_lowercase)
    result = []
    for n in arpabet:
        idx = inputList.index(n) if n in inputList else -1
        result.append(str(idx))
    print(' '.join(result))

def main():
    X = input()
    solve(X)

if __name__ == "__main__":
    main()