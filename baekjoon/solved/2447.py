import math

def print_start_list(data):
    for x in data:
        p = ''
        for n in x:
            p += n
        print(p)

def get_star_list(data):
    result = []
    loop_cnt = 3
    for n in range(loop_cnt):
        for i in data:
            if n == 1:
                result.append(i + ([' '] * len(data[0])) + i)
            else:
                result.append(i * loop_cnt)
    return result

# k = [1, 2, 3, 4, 5, 6, 7]
# N = [3, 9, 27, 81, 243, 729, 2187]          
def main():
    N = round(math.log(int(input()), 3))
    data = [['*']]
    for _ in range(1, N+1):
        data = get_star_list(data)
    print_start_list(data)
    
if __name__ == '__main__':
    main()