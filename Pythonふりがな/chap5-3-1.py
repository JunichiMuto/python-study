from datetime import date, timedelta

start = date(2019, 11, 24)
for d in range(14):
    cur = start + timedelta(days = d)
    print(cur)