with open("4.txt","r") as f:
    lines = f.readlines()
    lc = len(lines)
    wc = 0
    cc = 0
    for line in lines:
        wc += len(line.split())
        cc += len(line)
print(lc)
print(wc)
print(cc)