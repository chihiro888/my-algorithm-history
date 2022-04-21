def output(s):
    for d in s:
        for x in d:
            print(x, end='')
        print()
 
 
def simulation(s, mmm):
    for _ in range(mmm):
        for i in range(len(s)-1):
            for j in range(len(s[0])):
                if s[i][j] == '*' and s[i+1][j] == '.':
                    s[i][j] = '.'
                    s[i+1][j] = '*'
    return s
 
def main():
    t = int(input())
 
    for _ in range(t):
        n, m = map(int, input().split())
        s = []
        for _ in range(n):
            x = input()
            s.append([char for char in x])
        output(simulation(s, 50))
        print()
        
if __name__ == '__main__':
    main()