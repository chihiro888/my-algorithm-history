x = [int(d) for d in input()]
x.sort(reverse=True)

solve = ''
for d in x:
    solve += str(d)
    
print(solve)
