import os

file_path = "C:\\Users\\user\\Desktop\\test\\запрещенный файл\\new waaay\\DUMP_FILE.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted successfully.")
else:
    print("The file does not exist.")
