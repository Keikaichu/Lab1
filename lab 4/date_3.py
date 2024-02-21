import datetime
import time
new = datetime.datetime.now()
print("current time: ",new)
newest = new.strftime("%Y-%m-%d %H:%M:%S")
print("without milliseconds: ",newest)