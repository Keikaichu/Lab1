import os
f = open("C:\\Users\\user\\Desktop\\test\\запрещенный файл\\new waaay\\SOME_ANOTHER_FILE.txt")
f2 = "C:\\Users\\user\\Desktop\\test\\запрещенный файл\\new waaay\\SOME_THIRD_FILE.txt"
content = f.read()
new_list = []
for x in content:
    new_list.append(x)

with open(f2, "w") as y:
    for x in new_list:
        y.write(x)
