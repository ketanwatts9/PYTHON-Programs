#1
# m1 = int(input())
# m2 = int(input())
# m3 = int(input())
# m1, m2, m3 = map(int,input().split())
# if m1>=40 and m2>=40 and m3>=40:
#     print("PASS")
# else:
#     print("FAIL")

#2
# amount = int(input())
# if amount>=5000:
#     discount = 0.2*amount
# elif amount<=5000 and amount>=2000:
#     discount = 0.1*amount
# elif amount<2000:
#     discount = 0
# final = amount - discount
# print(final)

#3
# day = int(input())
# match day:
#     case 1|2|3|4|5:
#         print("Weekday")
#     case 6|7:
#         print("Weekends")
#     case _:
#         print("invalid input")

#4
# n = int(input())
# i = 2
# while i<=n:
#     if i%2==0:
#         print(i)
#     i+=1

#5
# n = int(input())
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(sum)

#6
# n = int(input())
# if n == 0:
#     print("Zero")
# else:
#     if n>0:
#         print("Positive")
#     else:
#         print("Negative")

#7
# r = int(input())
# c = int(input())
# for i in range(r):
#     for j in range(c):
#         print("*",end=' ')
#     print()

#8
# n = int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

#9
# n = int(input())
# for i in range(n+1):
#     if i%3==0:
#         continue
#     else:
#         print(i)

#10
# n = int(input())
# num = list(map(int,input().split()))
# for i in num:
#     if i<0:
#         break
#     print(i)

#11
# n = int(input())
# for i in range(1,n+1):
#     if i == 5:
#         pass
#     print(i)

#12
# def add_numbers(a,b):
#     return a+b
# a,b = map(int,input().split())
# result = add_numbers(a,b)
# print(result)

#13
# def print_student(name,age):
#     print(f"Name: {name}, Age: {age}")
# name = input()
# age = int(input())
# print_student(name,age)

#14
# def power(base,exp=2):
#     return base**exp
# base = int(input())
# exp = input()
# if exp == "":
#     print(power(base))
# else:
#     print(power(base,int(exp)))

#15
# def total(nums):
#     s = 0
#     for i in nums:
#         s += i
#     return s
# n = int(input())
# nums = map(int,input().split())
# print(total(nums))

#16
# counter = 0 
# def increment():
#     global counter
#     counter += 1
#     return counter
# print(counter)
# print(increment())
# print(increment())
# print(increment())
# print(increment())

#17
# def factorial(n):
#     if n < 0:
#         return "invalid input"
#     if n == 0 or n ==1:
#         return 1
#     else:
#         return n * factorial(n-1)
# n = int(input())
# print(factorial(n))    

#18
# double = lambda x: 2*x
# x = int(input())
# print(double(x))

#19
# def lst_sum(lst):
#     s = 0
#     for i in lst:
#         if lst == []:
#             return 0
#         else:
#             s+=i
#     return s
# lst = map(int,input().split())
# print(lst_sum(lst))

#20
# lst = list(map(int,input().split()))
# print("first element: ",lst[0])
# print("last element: ",lst[-1])
# print("remaning list: ",lst[1:-1])

#21
# n = int(input())
# nums = list(map(int,input().split()))
# new = [x*x for x in nums if x%2==0]
# print(*new)

#22
# n = int(input())
# nums = list(map(int, input().split()))
# new = list(map(lambda c: 1.8*c + 32,nums))
# print(*new)

#23
# from functools import reduce
# n = int(input())
# num = list(map(int,input().split()))
# filtered = list(filter(lambda x: x>=100,num))
# if filtered:
#     total = reduce(lambda x,y: x+y,filtered)
# else:
#     total  = 0
# print(total)

#24
# r,c = map(int,input().split())
# matrix = []
# for i in range(r):
#     row = list(map(int,input().split()))
#     matrix.append(sum(row))
# for i in matrix:
#     print(i)

#25
# r = int(input())
# jagged = []
# for i in range(1,r+1):
#     c = int(input())
#     row = list(map(int,input().split()))
#     jagged.append(row)
# for row in jagged:
#     print(len(row))

#26
# s = input().lower()
# total = 0
# for i in s :
#     if i in 'aeiou':
#         total+=1
# print(total)

#27
# s = input()
# new = [char for char in s if char != " "]
# print("".join(new))

#28
# s = input().lower()
# clean = ""
# for ch in s:
#     if ch != " ":
#         clean += ch
# if clean == clean[::-1]:
#     print("YES")
# else:
#     print("NO")

#29
# n = int(input())
# nums = tuple(map(int,input().split()))
# print("max:",max(nums))
# print("min:",min(nums))
# print("average:",sum(nums)/len(nums))

#30
# lstsent = input().split()
# stsent = set(lstsent)
# result = len(stsent)
# print(result)

#31
# s = input().strip()
# freq = {}
# for char in s:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1
# for ch in freq:
#     print(ch,freq[ch])

#32
# sent = input().split()
# result = {ch: len(ch) for ch in sent}
# for word in result:
#     print(word,result[word])

#33
# import random
# n = int(input())
# for i in range(1,n+1):
#     print(random.randint(1,6))

#34
# from math import sqrt,pi
# x = int(input())
# print(sqrt(x))
# print(pi)

#35
# n = int(input())
# with open("numbers.txt","w") as f:
#     for i in range(1,n+1):
#         f.write(str(i)+"\n")
# total = 0
# with open("numbers.txt","r") as f:
#     for line in f:
#         total += int(line)
# print(total)

#36
# k = int(input())
# with open("info.txt","r") as f:
#     c = f.read(k)
#     print(c)

#37
# a,b = map(int,input().split())
# try:
#     result = a/b
#     print(result)
# except ZeroDivisionError:
#     print("division by 0 is not allowed")

#38
# try:
#     num = int(input())
#     print("you entered",num)
# except ValueError:
#     print("invalid input")
# finally:
#     print("program end")

#39
# class UnderAgeError(Exception):
#     pass
# age = int(input())
# try:
#     if age < 18:
#         raise UnderAgeError
#     else:
#         print("eligible to vote")
# except UnderAgeError:
#     print("uder age for voting")

#40
# class person:
#     def __init__(self,name):
#         self.name = name
#     def describe(self):
#         print(f"person: {self.name}")
# class student(person):
#     def __init__(self, name,grade):
#         super().__init__(name)
#         self.grade = grade
#     def describe(self):
#         print(f"student: {self.name}, grade: {self.grade}")
# name = input()
# grade = input()
# s = student(name,grade)
# s.describe()
# print("is person?",isinstance(s,person))