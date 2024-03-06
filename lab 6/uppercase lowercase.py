x = input()
counter = 0
counter2 = 0
def newfunc(x):
    global counter, counter2
    for j in x:
        if j.isupper():
            counter += 1
        elif j.islower():
            counter2 += 1

newfunc(x)

print("Uppercase: ",counter)
print("Lowecase: ",counter2)
