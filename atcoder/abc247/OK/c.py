def P(N):
    if N == 1:
        return '1'
    else:
        return f'{P(N-1)} {N} {P(N-1)}'
    
def main():
    N = int(input())
    print(P(N))

if __name__ == "__main__":
    main()
    
'''
https://atcoder.jp/contests/abc247/submissions/30870650
'''