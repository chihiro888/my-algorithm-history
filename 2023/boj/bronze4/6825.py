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
    w = float(ip())
    h = float(ip())
    
    bmi = w / (h*h)
    
    if bmi > 25:
        print('Overweight')
    elif 18.5 <= bmi <= 25.0:
        print('Normal weight')        
    elif bmi < 18.5:
        print('Underweight')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------