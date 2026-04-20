import os

print(f"folder saat ini {os.getcwd()}")

print(f"sistem operasi {os.name}")

print("main.py", os.path.exists("main.py"))

file_path = "C:\MAYA2026\Python-Udemy\python-modules\main.py"
print("directory", os.path.dirname(file_path))
print("file", os.path.basename(file_path))
# menit 19
