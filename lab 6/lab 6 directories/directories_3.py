import os

file_path = "C:\\Users\\user\\Desktop\\test\\запрещенный файл\\new waaay"
file_name = "SOME_FILE.txt"

def check_for_existance(file_path):
    if os.path.exists(file_path):
        print("This path existz")
    else:
        print("Nuh-uh this path DOES NOT exist")
        return 0

check_for_existance(file_path)

print(f"Directory is: {file_path} ")
print(os.listdir(file_path))