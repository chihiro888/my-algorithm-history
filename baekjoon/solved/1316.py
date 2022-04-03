def groupWordChecker(data):
    cnt = 0
    useData = []
    prevData = None
    for d in data:
        if d not in useData:
            useData.append(d)
        elif (d in useData) and (d != prevData):
            cnt += 1
        prevData = d
    if cnt != 0:
        return False
    elif cnt == 0:
        return True

def main():
    N = int(input())

    cnt = 0
    for _ in range(0, N):
        if(groupWordChecker(input())):
           cnt +=1
    print(cnt)

if __name__ == "__main__":
    main()