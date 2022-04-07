import sys

data = []

def stack_program(command):
    if command.find('push') != -1:
        t = command.split()
        data.append(int(t[1]))
    elif command.find('pop') != -1:
        if len(data) == 0:
            print(-1)
        else:
            print(data[-1])
            data.pop()
    elif command.find('size') != -1:
        print(len(data))
    elif command.find('empty') != -1:
        if len(data) == 0:
            print(1)
        else:
            print(0)
    elif command.find('top') != -1:
        if len(data) == 0:
            print(-1)
        else:
            print(data[-1])

def main():
    N = int(input())
    for _ in range(N):
        command = sys.stdin.readline().strip()
        stack_program(command)
    
if __name__ == '__main__':
    main()