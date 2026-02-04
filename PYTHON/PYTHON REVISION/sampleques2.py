#1
# m1,m2,m3 = map(int,input().split())
# if m1>=40 and m2>=40 and m3>=40:
#     print("pass")
# else:
#     print('fail') 

#2
# a,b,c = map(int,input().split())
# if a>=b and a>=c:
#     print(a)
# elif b>=c and b>=a:
#     print(b)
# else:
#     print(c)

#3
# n = int(input())
# if n%2 == 0:
#     print("even")
# else:
#     print("odd")

#4
# n = int(input())
# if n == 0:
#     print("zero")
# elif n<0:
#     print("negative")
# else:
#     print("postive")

#5
# a = int(input())
# b = int(input())
# operator = input()
# if operator == "+":
#     print(a+b)
# elif operator == "-":
#     print(a-b)
# elif operator == "*":
#     print(a*b)
# elif operator == "/":
#     print(a/b)
# else:
#     print("invalid operator")

#6
# s= input().lower()
# sum = 0
# for ch in s:
#     if ch in 'aeiou':
#         sum+=1
# print(sum)

#7
# s = input().lower()
# if s == s[::-1]:
#     print("palindrome")
# else:
#    print("not palindrome")

#8
# n = int(input())
# marks = map(int,input().split())
# print(sum(marks))

#9
# s = input()
# st = set(s)
# print(len(st))

#10
# n = int(input())
# a,b = 0,1
# for i in range(1,n+1):
#     print(a,end=" ")
#     a,b = b,a+b

#11
# n = int(input())
# for i in range(1,n+1):
#     print(i,end=" ")

#12
# sum = 0
# i = 1
# n = int(input())
# while i <= n:
#     sum += i
#     i+=1
# print(sum)

#13
# fact = 1
# n = int(input())
# for i in range(1,n+1):
#     fact *= i
# print(fact)

#14
# n = int(input())
# print(len(str(n)))

#15
# n = int(input())
# rev = 0
# while n >0:
#     rev = rev*10 + n%10
#     n = n //10
# print(rev)
# n = int(input())
# print("".join(reversed(str(n))))

#16
# n = int(input())
# s = str(n)
# if s == s[::-1]:
#     print("palindrome")
# else:
#     print("not a palindrome")

#17
# n = int(input())
# for i in range(1,n+1):
#     if i%2!=0:
#         continue
#     else:
#         print(i)

#18
# n = int(input())
# for i in range(1,n+1):
#     if i %7==0:
#         break
#     else:
#         print(i,end = " ")

#19
# n = int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

#20
# n = int(input())
# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")

#21
# def check(n):
#     if n %2 == 0:
#         return 'even'
#     else:
#         return "odd" 
# print(check(4))
# print(check(7))

#22
# def maxi(lst):
#     return max(lst)
# n = int(input())
# lst = list(map(int,input().split()))
# print(maxi(lst))

#23
# def total(lst):
#     return sum(lst)
# n = int(input())
# lst = list(map(int,input().split()))
# print(total(lst))

#24
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1)+fib(n-2)
# n = int(input())
# for i in range(1,n+1):
#     print(fib(i),end=" ")

#25
# def sumn(n):
#     if n == 0:
#         return 0 
#     return n%10 + sumn(n//10)
# n = int(input())
# print(sumn(n))

#26
# sq = lambda x:x**2
# print(sq(33))

#27
# def unique(s):
#     found = set()
#     for i in s:
#         if i in "aeiou":
#             found.add(i)
#     print(len(found))
# s = input()
# unique(s)

#28
# def avg(lst):
#     return sum(lst)/len(lst)
# n = int(input())
# lst = list(map(int,input().split()))
# print(avg(lst))

#29
# x = 10
# def gbl(x):
#     x = 5
#     print("local: ",x)
# gbl(x)
# print("global: ",x)

#30
# def count_n(lst,n):
#     return lst.count(n)
# no = int(input())
# num = list(map(int,input().split()))
# n = int(input())
# print(count_n(num,n))

#31
# s = input()
# index = int(input())
# print(s[index])

#32
# s = input()
# print(s[::-1])

#33
# n = int(input())
# books_list = input().split()
# book_name = input()
# print(books_list.count(book_name))

#34
# n = int(input())
# marks = set(map(int,input().split()))
# print(marks)

#35
# variables = input().split()
# set_var = set(variables)
# print(len(set_var))

#36
# n = int(input())
# num = list(map(int,input().split()))
# print(tuple(num))

#37
# n = int(input())
# student_marks = {}
# for i in range(n):
#     name, marks = input().split()
#     student_marks[name] = int(marks)
# print(student_marks)

#38
# n = int(input())
# student_marks = {}
# for i in range(n):
#     name, marks = input().split()
#     student_marks[name] = int(marks)
# print(max(student_marks,key = student_marks.get))

#39
# n = int(input())
# lst = list(map(int,input().split()))
# final = [x*x for x in lst if x%2==0]
# print(final)

#40
# s = input().split()
# new = {}
# for ch in s:
#     if ch in new:
#         new[ch] += 1
#     else:
#         new[ch] = 1
# print(new)

#41
# import math
# n = int(input())
# print(math.sqrt(n))

#42
# import random
# print(random.randint(1,100))

#43
# s = input()
# with open("data.txt","w") as f:
#     f.write(s)

#44
# with open('data.txt',"r") as f:
#     c = f.read()
# print(c)

#45
# a = int(input())
# b = int(input())
# try:
#     result = a/b
# except ZeroDivisionError:
#     print('division by zero is not allowed')

#46
# try:
#     a = int(input())
#     b = int(input())
#     result = a/b
#     print(result)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# finally:
#     print("execution completed")

#47
# class AgeError(Exception):
#     pass
# try: 
#     age = int(input())
#     if age<18:
#         raise AgeError
#     else:
#         print("eligible to vote")
# except AgeError:
#     print("not eligible to vote")

#48
# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def details(self):
#         print(f"name: {self.name}, marks: {self.marks}")
# name = input()
# marks = int(input())
# s = student(name,marks)
# s.details()

#49
# class person:
#     def __init__(self,name):
#         self.name = name
# class student(person):
#     def __init__(self, name,marks):
#         super().__init__(name)
#         self.marks = marks
#     def display(self):
#         print(f'name: {self.name}, marks: {self.marks}')
# name = input()
# marks = int(input())
# s= student(name,marks)
# s.display()

#50
# class animal:
#     def speak(self):
#         print("animal make sound")
# class dog(animal):
#     def speak(self):
#         print("dog barks")
# d = dog()
# d.speak()