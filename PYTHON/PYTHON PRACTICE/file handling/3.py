import os
path = r"C:\Users\ketan\OneDrive\Desktop\PYTHON\PYTHON PRACTICE\file handling" 
for filename in os.listdir(path):
    if filename.endswith(".tmp"):
        os.remove(path + "\\" + filename)
        print(f"deleted {filename}")
