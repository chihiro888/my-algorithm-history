def solve(n):
    zero = 0
    while n >= 5:
        zero += n // 5
        n //= 5
    return zero


m = int(input())

r = 0
left = 1
right = m * 10

while left <= right:
    mid = (left + right) // 2
    # print(f'mid = {mid}')

    zero = solve(mid)
    # print(f'zero = {zero}')

    if zero < m:
        left = mid + 1
    else:
        right = mid - 1
        result = mid

print(result if solve(result) == m else -1)