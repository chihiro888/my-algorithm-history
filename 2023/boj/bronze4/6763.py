import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------

# -------------------------------


# Please write the code below ---
def main():
    limit = int(ip())
    speed = int(ip())
    
    if limit >= speed:
        print('Congratulations, you are within the speed limit!')
    else:
        over = speed - limit
        if 1 <= over and over <= 20:
            print(f'You are speeding and your fine is $100.')
        elif 21 <= over and over <= 30:
            print(f'You are speeding and your fine is $270.')
        elif 31 <= over:
            print(f'You are speeding and your fine is $500.')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------