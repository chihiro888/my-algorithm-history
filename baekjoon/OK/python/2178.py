def BFS(maze):
    # left/right/up/down
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    # BFS - queue
    queue = [(0, 0)]
    
    # BFS - visited counter
    maze[0][0] = 0
    
    # BFS
    while queue:
        x, y = queue.pop(0)
        
        # goal
        if x == len(maze)-1 and y == len(maze[0])-1:
            print(maze[x][y]+1)
            
        for i in range(4):
            # set next position
            nx = x + dx[i]
            ny = y + dy[i]
            # range over validation
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                # if not visited
                if maze[nx][ny] == 1:
                    # set visited
                    maze[nx][ny] = maze[x][y] + 1
                    
                    # append next position in queue
                    queue.append((nx, ny))

def main():
    # input
    n, m = map(int, input().split())
    
    # init maze
    maze = []
    for _ in range(n):
        d = input()
        maze.append([int(x) for x in d])
        
    BFS(maze)

if __name__ == '__main__':
    main()
