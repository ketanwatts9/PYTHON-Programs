#1
# salary = int(input())
# gender = input()
# if gender == "F":
#     c_salary = 0.15*salary
#     total = salary+c_salary
#     print(total)
# elif gender== "M":
#     c_salary = 0.10*salary
#     total = salary+c_salary
#     print(total)
# else:
#     print("wrong input")

#2
# days = int(input())
# if days>0 and days<=5:
#     fine = days*0.5
#     print("fine amount to pay: RS",fine)
# elif days>5 and days<=10:
#     fine = days*1
#     print("fine amount to pay: RS",fine)
# elif days>10 and days<=30:
#     fine = days*5
#     print("fine amount to pay: RS",fine)
# elif days>30:
#     print("your membership would be cancelled")

#3
# year = int(input())
# if year%4==0 and year%100!=0:
#     print(f"{year} is leap year")
# elif  year%400==0:
#     print(f"{year} is leap year")
# else:
#     print(f"{year} not a leap year")

#4
# r,c = map(int,input().split())
# matrix = []
# for rows in range(r):
#     row = list(map(int,input().split()))
#     matrix.append(row)
# sum = 0
# for i in range(r):
#     for j in range(c):
#         if i==0 or i==r-1 or j==0 or j==c-1:
#             sum += matrix[i][j]
# print(sum)

#5
# r = int(input())
# c = int(input())
# matrix = []
# for i in range(r):
#     row = list(map(int,input().split()))
#     maxi = max(row)
#     matrix.append(maxi)
# print(matrix)

#6
# r = int(input())
# c = int(input())
# matrix = eval(input())
# maxcol = [max(i) for i in list(zip(*matrix))]

#7
# s = input()
# if s == s[::-1]:
#     print(f"{s} is palindrome")
# else:
#     print(f"{s} is not palindrome")

#8
# s = input()
# count = 0
# for i in range(len(s)-1):
#     if s[i].islower() and s[i+1].isupper():
#         count+=1
# print(count)

#9
# s1 = input()
# s2 = input()
# l = len(s1)//2
# print(s1[:l]+s2+s1[l:])