with open("5.txt", "r") as f:
    c = f.read()
with open("5copy.txt", "w") as f:
    f.write(c)