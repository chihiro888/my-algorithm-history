while (True):
    s = input()
    if s == '0': break
    solve = 'yes'
    for i in range((len(s) // 2)):
        if s[i] != s[-1 * (i + 1)]:
            solve = 'no'
    print(solve)