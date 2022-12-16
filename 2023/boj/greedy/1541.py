import sys


# Utilities ---------------------
debug = True
def p(name, value):
    if debug: print(f'{name} = {value}')
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
# -------------------------------


# Function Block ----------------
def string_to_list(s):
    d = [i for i in s]
    d.append('E')
    dd = []
    x = ''
    for t in d:
        if not (t == '-' or t == '+' or t == 'E'):
            x += t
        else:
            dd.append(int(x))
            dd.append(t)
            x = ''
    dd.pop()
    return dd

def solve(s):
    d = string_to_list(s)

    while d.count('+') != 0:
        i = d.index('+')
        d[i-1] = d[i-1] + d[i+1]
        del d[i:i+2]

    while d.count('-') != 0:
        i = d.index('-')
        d[i] = -1 * d[i+1]
        del d[i+1]

    return sum(d)
# -------------------------------


# Test --------------------------
def test_case1():
    r = solve('55-50+40')
    assert r == -35

def test_case2():
    r = solve('10+20+30+40')
    assert r == 100

def test_case3():
    r = solve('00009-00009')
    assert r == 0

def test_case4():
    r = solve('10+50-100+150')
    assert r == -190

def test_case5():
    r = solve('10-50+100+150')
    assert r == -290

def test_case6():
    r = solve('10-50+100-5')
    assert r == -145
# -------------------------------


# Please write the code below ---
def main():
    s = ip()
    r = solve(s)
    print(r)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------