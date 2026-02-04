#1
# num=int(input("enter your number:"))
# if num%2==0:
#     print("number is even")
# else:
#     print("number is odd")

#2
# num=int(input("enter your number:"))
# if num>0:
#     print("number is positive")
# elif num==0:
#     print("number is zero")
# else:
#     print("number is negative")

#3
# age=int(input("enter your age:"))
# if age>=18:
#     print("eligible to vote")
# else:
#     print("not eligible")

#4
# year=int(input("enter your year:"))
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("Leap year")
# else:
#     print("Not a leap year")

#5
# num=int(input("enter your number:"))
# if num%5==0 and num%11==0:
#     print("number is divisible by both 5 and 11")
# else:
#     print("number is not divisible by 5 and 11")

#6
# a=int(input('enter first number:'))
# b=int(input('enter second number:'))
# if(a>b):
#     print("a is larger")
# elif(a==b):
#     print("both and b is equal")
# else:
#     print("b is larger")

#7
# char=input("enter single character:")
# if len(char)==1:
#     if char.isupper():
#         print("it is uppercase chracter")
#     elif char.islower():
#         print("it is lowercase chracter")
#     else:
#         print("it is not an alphabetical chracater" )
# else:
#     print("enter input of single character")

#8
# num=int(input("enter a number:"))
# if num<0:
#     absolute_value=-num
#     print("absolute value is :",absolute_value)
# else:
#     print("absolute value is :",num)

#9
# a=int(input("enter a number:"))
# if (a%3==0) and (a%7==0):
#     print("it is a multiple of both 3 and 7")
# elif a%3==0:
#     print("it is a multiple of 3")
# elif a%7==0:
#     print("it is a multiple of 7")
# else:
#     print("it is not multiple of both")

#10
# year = int(input("Enter a year: "))
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("It is a leap year")
# else:
#     print("It is not a leap year")

#11
# marks=int(input('enter your marks:'))
# if marks>=90:
#     print("grade a")
# elif marks>=80:
#     print("grade b")
# elif marks>=70:
#     print("grade c")
# elif marks>=60:
#     print("grade d")
# else:
#     print("grade f")

#12
# unit=int(input('enter units consumed:'))
# if unit<=100:
#     total=unit*1.0
#     print(total)
# elif unit>100:
#     total=unit*1.5
#     print(total)
# elif unit>200:
#     print(unit*2.0)
# else:
#     print(unit*2.25)

#13
# print("--------simple calculator--------")
# print("1. add")
# print("2. sub")
# print("3. div")
# print("4. mul")
# print("5. exit")
# choice=int(input("enter your choice(1-5):"))
# if choice==5:
#     print("you are exiting from calculator, thankyou for using this!!!!!!")
# else:
#     a=int(input("enter first number:"))
#     b=int(input("enter second number:"))
#     if choice==1:
#         print("your answer is:",a+b)
#     elif choice==2:
#         print("your answer is:",a-b)
#     elif choice==3:
#         print("your answer is:",a/b)
#     elif choice==4:
#         print("your answer is:",a*b)
#     else:
#         print("invalid choice, try again")

#14
# temp=float(input("enter temperature(in celcius):"))
# if temp<=0:
#     print("freezing")
# elif temp>0 and temp<=15:
#     print("cold")
# elif temp>15 and temp<=30:
#     print("warm")
# else:
#     print("hot")

#15
# amount=int(input("enter total amount:"))
# if amount>=10000:
#     discount=amount*0.30
# elif amount>=5000:
#     discount=amount*0.20
# elif amount>=1000:
#     discount=amount*0.10
# else:
#     discount=0
# print("your discount is:",discount)
# total=discount+amount
# print("your amount to be paid:",total)

#16
# a=int(input("enter side one:"))
# b=int(input("enter side two:"))
# c=int(input("enter side three:"))
# if a==b==c:
#     print("triangle is equitorial")
# elif a==b or b==c or a==c:
#     print("triangle is isosceles")
# else:
#     print("triangle is scalene")

#17
# ch=input("enter your character:")
# if ch.isalpha():
#     print("it is an alphabet")
# elif ch.isdigit():
#     print("it is an number")
# else:print("it is an special character")

#18
# day=int(input("enter day(1-7):"))
# if day==1:
#     print("monday")
# elif day==2:
#     print("tuesday")
# elif day==3:
#     print("wednesday")
# elif day==4:
#     print("thursday")
# elif day==5:
#     print("friday")
# elif day ==6:
#     print("saturday")
# elif day==7:
#     print("sunday")
# else:
#     print("You entereed invalid choice")

#19
# w=int(input("enter your weight(in kg):"))
# h=int(input("enter your height(in m):"))
# bmi=h/w**2
# if bmi<18.5:
#     category="underweight"
# elif bmi<25.0:
#     category="normal"
# elif bmi<30:
#     category="overweight"
# else:
#     category="obese"
# print("calculated bmi is :",bmi)
# print("category acxording to bmi is:",category)

#20
# percentage=int(input("enter your marks(in %):"))
# if percentage>90:
#     print("distinction")
# elif percentage>80:
#     print("first position")
# elif percentage>50:
#     print("pass")
# else:
#     print("fail")

#21
# a=int(input('enter first number:'))
# b=int(input('enter second number:'))
# c=int(input('enter third number:'))
# if a>=b:
#     if a>=c:
#         largest=a
#     else:
#         largest=c
# else:
#     if b>=c:
#         largest=b
#     else:
#         largest=c
# print("largest number is=",largest)

#22
# marks=int(input("enter your marks:"))
# if marks<33:
#     print("fail")
# else:
#     if marks>=75:
#         print('distinction')
#     else:
#         print("pass")

#23
# a=int(input('enter first side:'))
# b=int(input('enter second side:'))
# c=int(input('enter third side:'))
# if a+b>c and b+c>a and a+c>b:
#     if a==b==c:
#         print("triangle is equitorial")
#     elif a==b or b==c or a==c:
#         print("triangle is isosceles")
#     else:
#         print("triangle is scalene")
# else:
#     print("triangle is invalid as per given sides")

#24
# balance = float(input("enter balance amount:"))
# widrawl= float(input("enter widrawl amount:"))
# if widrawl%100!=0:
#     print("invalid amount, widrawl amount shoould be divisible by 100")
# else:
#     if widrawl>balance:
#         print("insufficient balance")
#     else:
#         balance=balance-widrawl
#         print("amount widrwal successful")
#         print("amount balance:",balance)

#25
# username=input("enter your username:")
# password=input("enter your password:")
# if username=="admin":
    # if password=="1234":
        # print("login successful")
    # else:
        # print("wrong password")
# else:
    # print("wrong username")

#26
# year=int(input("enter year:"))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("leap year")
#         else:
#             print("not a leap year")
#     else:
#         print("leap year")
# else:
#     print("not a leap year")

#27 
# salary=int(input("enter your salary:"))
# experience=int(input("enter years of experience:"))
# if experience>5:
#     bonus=salary*0.10
# else:
#     bonus=salary*0.05
# print("your bonus is:",bonus)
# print("total amount",salary+bonus)

#28
# attendence=int(input("enter your attendence:"))
# if attendence<75:
#     medical=input("do you have medical certificate (yes/no):")
#     if medical.lower()=="yes":
#         print("you are allowed to sit in exam.")
#     else:
#         print("you are not allowed to sit in exam")
# else:
#     print("you are allowed to sit in exam")

#29
# age=int(input("enter your age:"))
# if age<18:
#     print("you are not eligible for licence")
# else:
#     test=input("do you passed the driving test(yes/no):")
#     if test.lower()=="yes":
#         print("your licence is approved")
#     else:
#         print("your licence is not approved")

#30
# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# c=int(input("enter third number:"))
# if a>b:
#     if a>c:
#         maximum=a
#     else:
#         maximum=c
# else:
#     if b>c:
#         maximum=b
#     else:
#         maximum=c
# if a<b:
#     if a<c:
#         minimum=a
#     else:
#         minimum=c
# else:
#     if b<c:
#         minimum=b
#     else:
#         minimum=c
# print("maximum number is:",maximum)
# print("minimum number is:",minimum)

#31
# day=int(input("enter day(1-7): "))
# match day:
#     case 1:
#         print("monday")
#     case 2:
#         print("tuesday")
#     case 3:
#         print("wednesday")
#     case 4:
#         print("thursday")
#     case 5:
#         print("friday")
#     case 6:
#         print("saturday")
#     case 7:
#         print("sunday")
#     case _:
#         print("invalid choice")

#32
# month=input("enter month name :")
# match month:
#     case "january"|"march"|"may"|"july"|"august"|"october"|"december":
#         days=31
#     case "february":
#         days=28
#     case "april"|"june"|"september"|"november":
#         days=30
#     case _:
#         days=None
# print(f"number of days in {month} is: {days}")

#33
# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# operator=input("enter your operator:")
# match operator:
#     case "+":
#         ans=a+b
#     case "-":
#         ans=a-b
#     case "*":
#         ans=a*b
#     case "/":
#         ans=a/b
#     case _:
#         ans="none as invalid operator is used"
# print("your answe is:",ans)

#34
# ch=input("enter your letter:")
# match ch:
#     case "a"|"e"|"i"|"o"|"u":
#         print("it is a vowel")
#     case _:
#         print("it is a consonant")

#35
# light=input("enter colour of traffic light:")
# match light:
#     case "red":
#         print("stop")
#     case "yellow":
#         print("wait")
#     case "green":
#         print("go")

#36
# item=int(input("enter menu choice (1-4):"))
# match item:
#     case 1:
#         print("maggie")
#     case 2:
#         print("coffe")
#     case 3:
#         print("chocolate")
#     case 4:
#         print("tea")
#     case _:
#         print("invalid choice")

#37
# plan=int(input("enter plan number for details(1-3):"))
# match plan:
#     case 1:
#         print("plan details:")
#         print("cost = rs 200")
#         print("validity = 20 days")
#         print("data = 20 MB")
#     case 2:
#         print("plan details:")
#         print("price = rs 500")
#         print("validity = 50 days")
#         print("data = 50 MB")
#     case 3:
#         print("plan details:")
#         print("price = rs 1000")
#         print("validity = 100 days")
#         print("data = 100 MB")
#     case _:
#         print("invalid plan")


#38
# grade = input("enter your grade to check remark:")
# match grade:
#     case "A":
#         print("excellent")
#     case "B":
#         print("good")
#     case "C":
#         print("average")
#     case "D":
#         print("bad")
#     case "E":
#         print("very bad")
#     case "F":
#         print("fail")
#     case _:
#         print("invalid choice")

#39
# browser = input("enter browswer name:")
# match browser:
#     case "chrome":
#         print("launching chrome")
#     case "firefox":
#         print("launching firefox")
#     case "edge":
#         print("launching edge")
#     case _:
#         print("invalid choice")

#40
# marks = int(input("enter your marks to check grade:"))
# match marks:
#     case _ if marks in range(81,101):
#         print("GRADE A")
#     case _ if marks in range(51,81):
#         print("GRADE B")
#     case _ if marks in range(33,51):
#         print("GRADE C")
#     case _ if marks in range(0,33):
#         print("GRADE F")
#     case _:
#         print("INVALID CHOICE")
