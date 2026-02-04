#1
# print('my name is ketan')
# print('i am student of chitkara university')
# print('my branch is computer science')

# 2
# print('''hello everyone!
        #  my name is ketan
        #  and im student of
        #  chitkara university from
        #  computer science branch''')

# 3
# print("This is a message with a tab:\tAnd this is after the tab.\nThis is on a new line.")
# print("slash n is used for \t space")
# print("slash t is udes for \n new line")

#4
# age=int(input('enter age'))
# if age<18:
# print('you are not eligible to vote') #this is incorrect because of identation

#5
#comments are not included in code while executing it
"""it can be wriiten in 
two ways that is one is using 
hashtag and another one is by using
triple quotes"""

#6
# # Using default sep and end
# print("Hello", "World")
# # Using a custom separator
# print("Apple", "Banana", "Cherry", sep=" - ")
# # Using a custom end character
# print("This is the first part.", end=" ")
# print("This is the second part.")
# # Using both custom sep and end
# print("One", "Two", "Three", sep="|", end="!!!\n")
# print("Another line.")
# # Printing items without any separator
# print("P", "Y", "T", "H", "O", "N", sep="")

#7
# print("hello",end=" ")
# print("world")

#8
# print("1,2,3,4,5,6,7,8" ,sep=" , ")

#9
# print('first output')
# print()
# print('second output')

#10
# print('this is a multiline' \
#       ' and we can print many' \
#       ' lines using sinle print')

#11
# a,b,c=1,2,3
# print(a)
# print(b)
# print(c)

#12
# x=10
# print(x)
# x=14
# print(x)
# x+=x
# print(x)

#13
# a=1
# b=1.0
# c='1'
# d=True
# e=None
# print(f"value of a is {a} and its type is {type(a)}")
# print(f"value of b is {b} and its type is {type(b)}")
# print(f"value of c is {c} and its type is {type(c)}")
# print(f"value of d is {d} and its type is {type(d)}")
# print(f"value of e is {e} and its type is {type(e)}")

#14
# x=1
# print(f"value of x is {x} and its type is {type(x)}")
# x=1.0
# print(f"new value of x is {x} and its type is {type(x)}")
# x='10'
# print(f"another new value of x is {x} and its type is {type(x)}")
# x=None
# print(f"another value of x is {x} and its type is {type(x)}")
# x=True 
# print(f"yet another new value of x is {x} and its type is {type(x)}")

#15
# a = 2 
# b=2.05
# print(f"value of a is {a} and its type is {type(a)}")
# print(f"value of b is {b} and its type is {type(b)}")

#16
# a,b=1,2
# print(a,b)
# a,b=b,a
# print(a,b)

#17
# a= int(input("enter your number="))
# print("square of your number is=",a**2)
# print("square of your number is=",a*a)

#18
# global_var="i am global"
# def my_func():
#     print(global_var)
# my_func()
# print(global_var)

# def my_func():
#     a="i am local"
#     print(a)
# my_func()
# print(a) #this will give error

#19
# glovar=0
# def fummy():
#     global glovar
#     glovar=1
# fummy()
# print(glovar)

#20
# a=10
# b=20.0
# print(f"value of a is {a} before converting and its type is {type(a)}")
# print(f"value of b is {b} before converting and its type is {type(b)}")
# a=float(a)
# b=int(b)
# print(f"value of a is {a} after converting and its type is {type(a)}")
# print(f"value of b is {b} after converting and its type is {type(b)}")

#21
# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# print("sum of a and b is:",a+b)
# print("sub of a and b is:",a-b)
# print("mul of a and b is:",a*b)
# print("div of a and b is:",a/b)

#22
# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# print("floor division of a and b is:",a//b)
# print("modulus of a and b is:",a%b)

#23
# num=int(input("enter your power:"))
# power=int(input("enter its power:"))
# print(f"number is {num} and its power is {power} and is answer is {num**power}")

#24
# l=int(input("enter lenghth of rectangle:"))
# b=int(input("enter breadth of rectangle:"))
# print("area of rectangle is:",l*b)

#25
# r=int(input('enter radius of circle:'))
# print("perimeter of circle is:",2*3.14*r)

#26
# c=float(input("enter celcius temperature:"))
# print("temperature in fahernheit is:", (9/5)*c+32)

#27
# p=int(input("enter principal:"))
# r=int(input("enter rate:"))
# t=int(input("enter time:"))
# print("simple interest is:",(p*r*t)/100)

#28
# p=int(input("enter principal:"))
# r=int(input("enter rate:"))
# t=int(input("enter time:"))
# a = p * (1 + r/100) ** t
# ci = a - p
# print("compound interest:",ci)

#29
# second=int(input("enter seconds="))
# minute=second//60
# hour=minute//60
# print("minutes are:",minute)
# print("hours are",hour)

#30
# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# c=int(input("enter third number:"))
# avg=(a+b+c)/3
# print("average of three nubers is:",avg)

#31
# a=2
# a+=a
# print(a)
# a=2
# a-=a
# print(a)
# a=2
# a*=a
# print(a)
# a=2
# a/=a
# print(a)

#32
# a=2
# b=3
# print(a>b)
# print(a<b)
# print(a==b)
# print(a!=b)
# print(a>=b)
# print(a<=b)

#33
# a=2
# b=3
# print(a>b or a<b)
# print(a>b and a<b)
# print(not a<b)

#34
# result = 10 + 5 * 2 - 8 / 4 + (3 ** 2)
# print(f"The result of the expression is: {result}")

#35
# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# print("remainder of these numbers is :",a%b)
# print("quotient of these numbers is :",a//b)

#36
# a=int(input("enter number:"))
# print("square of number:",a**2)
# print("cube of number:",a**3)

#37
# base=float(input("enter base of triangle:"))
# height=float(input("enter height of triangle:"))
# area=0.5*base*height
# print("area of tiangle:",area)

#38
# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the rate of interest (in %): "))
# time = float(input("Enter the time period (in years): "))
# simple_interest = (principal * rate * time) / 100
# print("The Simple Interest is:", simple_interest)

#39
# distance=float(input("enter distance covered(in m):"))
# time=float(input("enter time(in sec):"))
# speed=distance/time
# print("speed:",speed)

#40
# kilometer=float(input("enter kilometers:"))
# conversion_factor=0.621371
# miles=kilometer*conversion_factor
# print(f"{kilometer} kilometers in miles is {miles} miles")

#41
# hours=float(input("enter number of hours:"))
# seconds=hours*3600
# print(f"{hours} hours is equals to {seconds} seconds")

#42
# a=float(input("enter marks of subject 1:"))
# b=float(input("enter marks of subject 2:"))
# c=float(input("enter marks of subject 3:"))
# d=float(input("enter marks of subject 4:"))
# e=float(input("enter marks of subject 5:"))
# total=a+b+c+d+e
# avg=total/5
# print(f"total of all five subjects is: {total} and average is: {avg}")

#43
# r=float(input("enter value of radius:"))
# h=float(input("enter height:"))
# v=3.14*(r**2)*h
# print("volume  of cylinder:",v) 

#44
# weight=float(input("enter weight(in kg):"))
# height=float(input("enter height(in m):"))
# bmi=weight/(height**2)
# print("body mass index=",bmi)

#45
# r=float(input("enter radius of circle:"))
# area=(22/7)*r*r
# circumference=(22/7)*2*r
# print("area=",area)
# print("circumference",circumference)

#46
# a=1
# b=3
# c="3"
# d=None
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))

#47
# name,age=input("enter name and age:").split()
# age=int(age)
# print("name:",name)
# print("age:",age)

#48
# import math
# n=int(input("enter your number:"))
# print("square root of number is :",math.sqrt(n))
# print("factorial of your number is:",math.factorial(n))

#49
# import datetime
# now=datetime.datetime.now()
# print("date and time is:",now)

#50
# import keyword
# print("python keywords are ",keyword.kwlist)