inputList = []
for n in range(0, 10):
    inputList.append(int(input()) % 42)

print(len(list(set(inputList))))