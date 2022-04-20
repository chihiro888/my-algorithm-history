import datetime
 
ay, am, ad = map(int, input().split())
by, bm, bd = map(int, input().split())

a = datetime.datetime(ay, am, ad)
b = datetime.datetime(by, bm, bd)
d_day = str(b-a).split()[0]

if int(d_day) > 365242:
    print('gg')
else: 
    print(f'D-{d_day}')