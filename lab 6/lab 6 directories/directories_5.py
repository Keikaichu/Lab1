import os

new_list = ['Watermelon','Banana','Kupupu']

file_path = "C:\\Users\\user\\Desktop\\test\\запрещенный файл\\new waaay\\Kupupa.txt"

with open(file_path, "w") as y:  #with - provides closure of file after ze wrok is done
    for x in new_list:
        y.write(x + " ")
