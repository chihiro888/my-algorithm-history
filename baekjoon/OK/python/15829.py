import sys
import string 

n = int(sys.stdin.readline().strip())
sList = [char for char in sys.stdin.readline().strip()]
idx = 0
sum = 0
for x in sList:
    d = string.ascii_lowercase.find(x) + 1
    sum += (d * (31 ** idx))
    idx += 1

print(sum % 1234567891)
