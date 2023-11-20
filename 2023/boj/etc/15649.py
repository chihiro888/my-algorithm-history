from itertools import permutations

def generate_sequences(N, M):
    numbers = list(range(1, N + 1))
    sequences = permutations(numbers, M)

    for seq in sequences:
        print(" ".join(map(str, seq)))

# 입력 받기
N, M = map(int, input().split())

# 수열 생성 및 출력
generate_sequences(N, M)