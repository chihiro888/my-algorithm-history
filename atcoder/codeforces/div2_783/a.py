'''
<Condition>

first (1, 1)
goal (n, m)

up (a-1, b)
down (a+1, b)
left (a, b-1)
right (a, b+1)

1. you cannot move in the same direction in two consecutive moves
2. you cannot leave the grid
3. What is the minimum number of moves to reach (n,m)?
* -1 if it is impossible to reach (n,m) under the given conditions
<Input>
6
1 1
2 1
1 3
4 2
4 6
10 5

<Output>
0
1
-1
6
10
17
'''
def BFS(n, m):
    # init visited list
    visited = [[0] * m for _ in range(n)]
    
    # left/right/up/down
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    # BFS - queue
    queue = [(0, 0, 9)]
    
    # BFS - visited counter
    visited[0][0] = 1
    
    # BFS
    while queue:
        x, y, prevIdx = queue.pop(0)
        
        # goal
        if x == n-1 and y == m-1:
            # return solution
            return visited[x][y]-1
            
        for i in range(4):
            # set next position
            nx = x + dx[i]
            ny = y + dy[i]
            # range over validation and move limit validation
            if 0 <= nx < n and 0 <= ny < m and i != prevIdx:
                # if not visited
                if visited[nx][ny] == 0:
                    # set visited
                    visited[nx][ny] = visited[x][y] + 1
                    
                    # append next position in queue
                    queue.append((nx, ny, i))

def main():
    # 1 <= t <= 1000
    t = int(input())

    for _ in range(t):
        # 1 <= n, m <= 1000000000
        n, m = map(int, input().split())

        solution = BFS(n, m)
        if solution == None:
            print(-1)
        else:
            print(solution)

if __name__ == '__main__':
    main()
