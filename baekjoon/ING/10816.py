def binary_search(arr, low, high, x):
    # print(f'arr = {arr}, low = {low}, high = {high}, x = {x}')
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

# 1 <= n <= 500,000
n = int(input())
# -10,000,000 <= x[i] <= 10,000,000
x = list(map(int, input().split()))
# 1 <= m <= 500,000
m = int(input())
# -10,000,000 <= y[i] <= 10,000,000
y = list(map(int, input().split()))

# print(f'n = {n}')
# print(f'x = {x}')
# print(f'm = {m}')
# print(f'y = {y}')

x.sort()
search_list = []
for t in y:
    startIdx = 0
    while True:
        # print(f't = {t}')
        i = binary_search(x, startIdx, len(x)-1, t)
        # print(f'i = {i}')
        if i == -1:
            break
        search_list.append(x[i])
        startIdx = i + 1
        # print(f'x = {x}')
        # print(f'search_list = {search_list}')
        # print('--------------------------')
    # d = x.count(t)
    # print(d, end=' ')
# print(f'search_list = {search_list}')

for t in y:
    print(search_list.count(t), end=' ')