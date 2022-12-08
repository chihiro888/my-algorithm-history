import copy

def solve(d):
    idx = 0
    for x in d:
        t = copy.deepcopy(d)
        del t[idx]
        t = set(t)
        # print(f't = {t}')
        print(x - max(t), end=' ')
        idx += 1
    print()
 
 
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        d = list(map(int, input().split()))
        solve(d)
 
if __name__ == "__main__":
    main()