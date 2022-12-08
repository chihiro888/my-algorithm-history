def main():
    n = int(input())
    for _ in range(n):
        s = int(input())
        d = input()
        xList = []
        for letter in d:
            x = ord(letter) - 96
            xList.append(x)
        
        print(max(xList))

if __name__ == "__main__":
    main()