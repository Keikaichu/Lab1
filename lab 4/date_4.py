import datetime
import time
a = time.localtime()
b = time.mktime(a)
print(b)

a_2 = "24 January 1999"
b_4 = time.strptime(a_2,"%d %B %Y")
b_5 = time.mktime(b_4)
print(b_5)

x = b - b_5
x_2 = datetime.timedelta(seconds=x)
print(x_2.total_seconds())
# print(b)