import sys


def get_lan_count(d, value):
    lan_count = 0
    for lan in d:
        lan_count += lan // value
    return lan_count


def get_mid(start, end):
    mid = (start + end) // 2
    return mid


def solve(d, n):
    start = 1
    end = max(d)
    
    while start <= end:
        mid = get_mid(start, end)

        lan_count = get_lan_count(d, mid)
        
        if lan_count < n:
            end = mid - 1
        else:
            start = mid + 1
            
    print(end)


def main():
    k, n = map(int, sys.stdin.readline().strip().split())
    d = []
    for _ in range(k):  
        d.append(int(sys.stdin.readline().strip()))
    
    solve(d, n)
    
            
if __name__ == "__main__":
    main()