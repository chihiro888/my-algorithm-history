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
    data = {
        'CU': 'see you',
        ':-)': 'I’m happy',
        ':-()': 'I’m unhappy',
        ';-)': 'wink',
        ':-P': 'stick out my tongue',
        '(~.~)': 'sleepy',
        'TA': 'totally awesome',
        'CCC': 'Canadian Computing Competition',
        'CUZ': 'because',
        'TY': 'thank-you',
        'YW': 'you’re welcome',
        'TTYL': 'talk to you later'
    }
    while True:
        s = ip()
        if s == '':
            break
        try:
            print(data[s])
        except KeyError:
            print(s)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------