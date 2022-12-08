h, w = map(int, input().split())
r, c = map(int, input().split())

left = (r, c-1)
right = (r, c+1)
up = (r-1, c)
down = (r+1, c)

solve = 0
if 0 < left[0] and left[0] <= h and 0 < left[1] and left[1] <= w:
    solve += 1    
if 0 < right[0] and right[0] <= h and 0 < right[1] and right[1] <= w:
    solve += 1
if 0 < up[0] and up[0] <= h and 0 < up[1] and up[1] <= w:
    solve += 1
if 0 < down[0] and down[0] <= h and 0 < down[1] and down[1] <= w:
    solve += 1
    
print(solve)