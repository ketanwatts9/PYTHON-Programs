#1,2,3
# s = int(input())
# total = 0
# current = 1
# for i in range(1,s+1):
#     if i%5 == 0:
#         current = 1
#     total += current
#     current *= 2
# print(total)    

#4,5,6
# mylist = eval(input())
# total = 0
# for i in mylist:
#     if i%1000 == 0:
#         total+=i//1000
#     else:
#         total+= (i//1000)+1
# print(total)

#7,8,9
# s = input().split()
# new = []
# for i in s:
#     for j in i:
#         if j in '$/*@#':
#             print("invalid symbol found")
#             exit()
#     new.append(i[::-1])
# print(*new)