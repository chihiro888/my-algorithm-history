import datetime

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

m, d = map(int, input().split())
x = datetime.datetime(2007, m, d)
print(days[x.weekday()])