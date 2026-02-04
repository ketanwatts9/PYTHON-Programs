count = 0
with open("10.log","r") as f,open("10e.txt", "w") as out:
    for line in f:
        if "ERROR" in line:
            out.write(line)
            count+=1
print(count)