names = eval(input())
with open("main.txt","w") as f:
    for name in names:
        f.write(name +"\n")
print("names added")
with open("main.txt","r") as f:
    a = len(f.readlines())
print(f"attendance recorded: {a} students")