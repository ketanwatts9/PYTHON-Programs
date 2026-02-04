with open("61.txt","r") as f:
    c1= f.read()
with open("62.txt","r") as f:
    c2= f.read()
with open("61+62.txt","w") as f:
    f.write(c1 +"\n")
    f.write(c2)