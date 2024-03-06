import os

""" os.R_OK: Check if the file is readable.
      
    os.W_OK: Check if the file is writable.
    
    os.X_OK: Check if the file is executable."""

file_path = "C:\\Users\\user\\Desktop\\test\\запрещенный файл"

def check_file_permissions(file_path):
   if os.path.exists(file_path):
      print(f"File exists")
   else:
      print(f"No such file in directory")
      return 0
   if os.access(file_path, os.R_OK):
      print(f"Read permission is granted for file: {file_path}")
   else:
      print(f"Read permission is not granted for file: {file_path}")

   if os.access(file_path, os.W_OK):
      print(f"Write permission is granted for file: {file_path}")
   else:
      print(f"Write permission is not granted for file: {file_path}")

   if os.access(file_path, os.X_OK):
      print(f"Execute permission is granted for file: {file_path}")

   else:
      print(f"Execute permission is not granted for file: {file_path}")

check_file_permissions(file_path)