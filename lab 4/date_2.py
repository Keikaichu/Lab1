import time
import datetime
today_base = time.localtime()
today = time.asctime(today_base)
today = time.strftime("%d %m %Y")
print("today:",today)

yesteday_base = datetime.datetime.now()
yesteday = yesteday_base - datetime.timedelta(days = 1)
yesteday_newone = yesteday.strftime("%d %m %Y")
print("yesterday:",yesteday_newone)

tommorow_base = datetime.datetime.now()
tommorow = tommorow_base + datetime.timedelta(days=1)
tommorow_newone = tommorow.strftime("%d %m %Y")
print("tomorrow:",tommorow_newone)