import os
trash = "boeuhu"
for files in os.listdir(trash):
    if files.endswith(".bak"):
        with open(f'{files}', "r") as f:
            c = f.read()
        with open(f"new{files}","w") as f:
            f.write(c)