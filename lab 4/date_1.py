# time() return the number of seconds
# ctime() return the current date
# sleep() stops execution of a thread for the given duration
# localtime() returns the date and time in time.struct_time format
# gmtime() returns time.struct_time in UTC format
# mktime() returns the seconds passes since epoch pas output
# asctime() returns a string representing the time
 
import time
# x = time.time()
# e = time.ctime(1708445588.6288855)
# c = time.localtime()
# # print(c)
# cc = time.asctime(c)
# print(cc)
# xx = time.strftime("%m/%d/%y")
# print(xx)
# y = "08 September 2006"
# yy = time.strptime(y,)
# print(yy)
import datetime

x = datetime.datetime.now()
newtime = x - datetime.timedelta(days = 5)
print(newtime)