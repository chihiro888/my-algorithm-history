def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

def main():
    # 1 <= N <= 100,000
    n = int(input())
    # -2^31 <= a[i] < 2^31
    # unsorted list
    a = list(map(int, input().split()))
    # 1 <= M <= 100,000
    m = int(input())
    # -2^31 <= b[i] < 2^31
    b = list(map(int, input().split()))

    a.sort()
    
    for x in b:
        if binary_search(a, x, 0, len(a)-1) != None:
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    main()