import time
import datetime
import math
x = int(input("enter num to square root:"))
y = int(input("enter miliseconds:"))
y_2 = y / 1000
time.sleep(y_2)
new_x = math.sqrt(x)
print("Square root of", x ,"after", y, "miliseconds is", new_x)
