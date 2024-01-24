x = "awesome"

def myfunc():
  global y
  y = "lol"
  print("Python is " + x)

myfunc()
print(y)
