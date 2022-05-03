def debug(maze):
    for m in maze:
        for n in m:
            print(n, end=' ')
        print()
    print('------------------')
        
def BFS(maze, k):
    # left/right/up/down
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    # BFS - queue
    queue = [(0, 0)]
    
    # BFS - visited counter
    maze[0][0] = 0
    
    round = 1
    
    # BFS
    while queue:
        # print(f'round = {round}')
        x, y = queue.pop(0)
        
        # goal
        if x == len(maze)-1 and y == len(maze[0])-1:
            return True
        
        # get magma index
        mi = 0
        magmaList = []
        for m in maze:
            mj = 0
            for n in m:
                if n == '@':
                    magmaList.append((mi, mj))
                mj += 1
            mi += 1
        
        # print(f'magmaList = {magmaList}')
        
        # movement - player 
        for i in range(4):
            # set next position
            nx = x + dx[i]
            ny = y + dy[i]
            # range over validation
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                # if not visited
                if maze[nx][ny] == '.':
                    # set visited
                    try:
                        maze[nx][ny] = maze[x][y] + 1
                    except BaseException:
                        return False
                    
                    # append next position in queue
                    queue.append((nx, ny))
        
        # movement - magma
        if round % k == 0:
            while magmaList:
                mx, my = magmaList.pop(0)
                for i in range(4):
                    nmx = mx + dx[i]
                    nmy = my + dy[i]
                    if 0 <= nmx < len(maze) and 0 <= nmy < len(maze[0]):
                        if maze[nmx][nmy] == '.' or isinstance(maze[nmx][nmy], int):
                            maze[nmx][nmy] = '@'
                            
        # debug(maze)                            
        round += 1 
                    
def main():
    # 2 <= h <= 2000
    # 2 <= w <= 2000
    # 1 <= k <= 2000
    h, w, k = map(int, input().split())

    # generate Dungeon
    dg = []
    for _ in range(h):
        dg.append([char for char in input().split()[0]])
    
    result = BFS(dg, k)
    if result:
        print('Yes')
    else:
        print('No')
        
if __name__ == '__main__':
    main()