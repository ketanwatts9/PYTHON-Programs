#1
# level = int(input())
# basic = float(input())
# rent = 0.25*basic
# if level == 1:
#     perks = 1500
# elif level == 2:
#     perks = 950
# elif level==3:
#     perks = 600
# elif level==4:
#     perks  = 250
# print(basic+rent+perks)

#2
# c = int(input())
# f = (1.8 *c)+32
# print(f)

#3
# m1 = int(input())
# m2 = int(input())
# m3 = int(input())
# m4 = int(input())
# m5 = int(input())
# total = m1+m2+m3+m4+m5
# avg = total/5
# print(total)
# print(avg)
# if avg>= 75:
#     print("Grade A")
# elif avg >= 60 and avg< 75:
#     print("Grade B")
# elif avg >= 55 and avg< 60:
#     print("Grade C")
# elif avg>= 50 and avg< 55:
#     print("Grade D")
# elif avg< 50:
#     print("Grade E")
# elif total == 0:
#     print("FAILED")

#4,5,6
# my_dict = eval(input())
# new = {}
# for i in my_dict:
#     for name,quantity in i.items():
#         if not isinstance(quantity,int):
#             print("Non-integer quantity skipped")
#         else:
#             if name in new:
#                 new[name] += quantity
#             else:
#                 new[name] = quantity
# print(new) 

#7,8,9
# t = eval(input())
# on = 0
# off = 0
# for i in t:
#     if i <=40 and i>0:
#         on +=1
#     elif i == -1:
#         break
#     else:
#         off += 1
# print(f"({on},{off})")