import os
file_path = r"C:\\Users\\user\\Desktop\\test\\запрещенный файл\\new waaay\\ABC.txt"
var = 97
new_list = []
while True:
    var2 = chr(var)
    new_list.append(var2)
    var += 1
    if var2 == 'z':
       break

with open(file_path, "w") as y:
    for x in new_list:
        y.write(x + ",")
