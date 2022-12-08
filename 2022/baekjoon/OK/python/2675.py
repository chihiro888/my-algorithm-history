import string

def split(word):
    return [char for char in word]
    
def solve(data):
    R = int(data[0])
    S = data[1]
    result = ''
    for x in split(S):
        result += (x * R)
    print(result)

def main():
    T = int(input())
    for n in range(0, T):
        data = input().split()
        solve(data)

if __name__ == "__main__":
    main()