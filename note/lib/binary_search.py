# 중복된 배열
# 왼쪽 인덱스 반환
def binary_search_left(d, t):
    start = 0
    end = len(d) - 1

    while start <= end:
        mid = (start + end) // 2

        if d[mid] < t:
            start = mid + 1
        else:
            end = mid - 1

    return start


# 중복된 배열
# 오른쪽 인덱스 반환
def binary_search_right(d, t):
    start = 0
    end = len(d) - 1

    while start <= end:
        mid = (start + end) // 2

        if d[mid] <= t:
            start = mid + 1
        else:
            end = mid - 1

    return end


# 중복되지 않은 배열
# 찾는 값이 있는 경우 인덱스 반환, 없는 경우 None 반환
def binary_search(d, t):
    start = 0
    end = len(d) - 1

    while start <= end:
        mid = (start + end) // 2

        if d[mid] > t:
            end = mid - 1
        elif d[mid] < t:
            start = mid + 1
        else:
            return mid


def main():
    t1 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
    t2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    t4 = [1, 2, 3, 5, 6, 7]
    
    print(binary_search_left(t1, 3))
    print(binary_search_right(t1, 3))
    print(binary_search(t2, 3))
    print(binary_search(t4, 4))
    

if __name__ == "__main__":
    main()