C4, A3, A4 = map(int, input().split())

a = C4 * 0.074196 * 2
b = A3 * 0.12474 * 2
c = A4 * 0.06237 * 1

print("{:6f}".format(round(a+b+c, 6)))