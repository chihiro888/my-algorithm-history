# https://www.acmicpc.net/board/view/86190

def main():
    # 1 <= M, N <= 500
    # 0 <= B <= 64000000
    n, m, b = map(int, input().split())

    # 1 <= x <= 250000
    # 0 <= x[i] <= 256
    x = []
    for _ in range(n):
        # O(500) -> O(N)
        x += list(map(int, input().split()))

    x.sort(reverse=True)
    
    # O(250000) -> O(N)
    minX = min(x)

    # O(250000) -> O(N)
    maxX = max(x)

    minTime = 999999999
    minFloor = 0
    for floor in range(minX, maxX+1):
        # O(256) -> O(N)
        time = 0
        block = b
        for xi in x:
            # O(250000) -> O(N)
            if xi > floor:
                time += (xi - floor) * 2
                block += (xi - floor)
            elif xi < floor:
                addBlock = floor - xi
                if (block - addBlock) >= 0:
                    time += addBlock
                    block -= addBlock
                else:
                    time = 999999999
        
        if minTime > time or (minTime == time and minFloor < floor):
            minTime = time
            minFloor = floor

    print(f'{minTime} {minFloor}')

if __name__ == '__main__':
    main()