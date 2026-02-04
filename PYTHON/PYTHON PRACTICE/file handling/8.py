with open("8.txt","r") as f:
    f.seek(0,2)
    size = f.tell()
    f.seek(0)
    first = f.read(20)
    last = f.read(size-20)
print(first)
print(last)