'''
input
4 6
101111
101010
101011
111011

maze
[
    [101111],
    [101010],
    [101011],
    [111011]
]
'''

def solve(maze, cnt, n, m, visited, position):
    
    # check the goal
    goal_n = len(maze)-1
    goal_m = len(maze[0])-1
    if n == goal_n and m == goal_m:
        print(f'(goal_n, goal_m) = ({goal_n}, {goal_m})')
        return False
    
    # count up
    cnt += 1
    
    # save history
    visited[n][m] = 1
    
    # save position
    position.append([n, m])
    
    # debug
    print('cnt = ', cnt)
    print(f'(n, m) = ({n}, {m})')
    print('------------------------------')
    
    # right
    if len(maze[n]) > m+1 and maze[n][m+1] != 0 and visited[n][m+1] != 1:
        m += 1
    # down
    elif len(maze) > n+1 and maze[n+1][m] != 0 and visited[n+1][m] != 1:
        n += 1
    # up
    elif 0 <= n-1 and maze[n-1][m] != 0 and visited[n-1][m] != 1:
        n -= 1
    else:
        position.pop()
        last_position = position.pop()
        n = last_position[0]
        m = last_position[1]
        cnt -= 1

    # recursive
    solve(maze, cnt, n, m, visited, position)

def main():
    '''
    # input
    N, M = map(int, input().split())

    # init maze
    maze = []
    for _ in range(N):
        maze.append(list(map(int, input().split())))
    '''
    
    maze = [
        [1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]
    ]
    
    visited = [[0]*6 for _ in range(4)]
    
    # solve
    solve(maze, 0, 0, 0, visited, [])

if __name__ == '__main__':
    main()
