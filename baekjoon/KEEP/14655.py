import copy

# b = copy.deepcopy(a)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(f'n = {n}')
print(f'a = {a}')
print(f'b = {b}')

a_d_m = 0
for i in range(0, n-2):
    a_d = copy.deepcopy(a)
    a_d[i] = a_d[i] * -1
    a_d[i+1] = a_d[i+1] * -1
    a_d[i+2] = a_d[i+2] * -1
    a_d_m = max(sum(a_d), a_d_m)

b_d_m = 999999
for i in range(0, n-2):
    b_d = copy.deepcopy(b)
    b_d[i] = b_d[i] * -1
    b_d[i+1] = b_d[i+1] * -1
    b_d[i+2] = b_d[i+2] * -1
    b_d_m = min(sum(b_d), b_d_m)

print(f'a_d_m = {a_d_m}')
print(f'b_d_m = {b_d_m}')
