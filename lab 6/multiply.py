
lst = []
z = 0
while True:
    x = int(input())
    lst.insert(0,x)
    z += 1
    if z == 5:
        break


y = 1
def multi(lst):
    global y
    for j in lst:
        y *= j

multi(lst)
print(y)
