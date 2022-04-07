N = int(input())

data_list = []
for _ in range(N):
    data_list.append(int(input()))
    
data_list.sort()

for data in data_list:
    print(data)