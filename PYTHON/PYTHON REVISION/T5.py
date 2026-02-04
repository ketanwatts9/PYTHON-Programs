#1,2,3
# from math import ceil
# energy = eval(input())
# strikes = int(input())
# newenergy=[]
# for e in energy:
#     if e>0:
#         newenergy.append(e)
# mapped_energy = list(map(lambda x:ceil(x/strikes),newenergy))
# print(len(newenergy))
# print(sum(mapped_energy))        

#4,5,6
# s = input()
# if s[:4] == "TKT-" and s[4:6].isdigit() and s[6:8].isupper:
#     print("VALID TICKET")
# else:
#     print("Bad Format")

#7,8,9
data = eval(input())
highearners = {}
update = {}
for name, money in data.items():
    pay,bonus = tuple(money)
    final = pay + (pay * bonus) / 100
    if final>20000:
        update[name] = final
        if final >50000:
            highearners[name] = final
print((update,highearners))