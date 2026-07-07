from datetime import datetime, date

now = datetime.now()
print(now)

t1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print(t1)

t_str = "5 December, 2019"
t_obj = datetime.strptime(t_str, "%d %B, %Y")
print(t_str)

d_now = date(year=2026, month=7, day=7)
new_year = date(year=2027, month=1, day=1)
diff = d_now-new_year
print(diff)

timestamp = now.timestamp()
print(timestamp)
