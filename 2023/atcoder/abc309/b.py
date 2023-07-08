import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
# 문자열을 리스트로 변환
def str_to_list(s:str):
    return [int(x) for x in s]

# 이차원 배열 디버깅
def print_arr(arr):
    for y in arr:
        for x in y:
            print(x, end='')
        print()

def rotate_outer_ring(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    rotated_matrix = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if i == 0 and j != cols - 1:
                rotated_matrix[i][j+1] = matrix[i][j]
            if i == rows - 1 and j != cols - 1:
                rotated_matrix[i][j] = matrix[i][j+1]
            if j == 0 and i != rows - 1:
                rotated_matrix[i][j] = matrix[i+1][j]
            if j == cols - 1 and i != rows - 1:
                rotated_matrix[i+1][j] = matrix[i][j]
            if 0 < i and i < rows-1 and 0 < j and j < cols-1:
                rotated_matrix[i][j] = matrix[i][j]

    return rotated_matrix
# -------------------------------


# Please write the code below ---
def main():
    size = int(ip())
    d = []
    for _ in range(size):
        x = ip()
        x = str_to_list(x)
        d.append(x)

    x = rotate_outer_ring(d)
    print_arr(x)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------