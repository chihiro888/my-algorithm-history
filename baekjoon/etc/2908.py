def split(word):
    return [int(char) for char in word]

D = list(map(int, input().split()))

A = split(str(D[0]))
B = split(str(D[1]))

A.reverse()
B.reverse()

A = int(str(A[0]) + str(A[1]) + str(A[2]))
B = int(str(B[0]) + str(B[1]) + str(B[2]))

if A > B:
    print(A)
elif A < B:
    print(B)
