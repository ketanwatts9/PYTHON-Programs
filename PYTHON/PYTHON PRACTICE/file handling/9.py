total = 0 
with open("9.txt","r") as f:
    for line in f:
        i,q,p = line.strip().split(",")
        total += int(q) *int(p)
with open("9p.txt", "w") as f:
    f.write(str(total))
