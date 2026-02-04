#1
# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def get_grade(self):
#         if self.marks >= 40:
#             print(f"{self.name} has passed")
#         else:
#             print(f"{self.name} has failed")
# s1 = student('ketan',43)
# s1.get_grade()

#2
# class employee:
#     def __init__(self,name,hours,rate):
#         self.name = name
#         self.hours = hours
#         self.rate = rate
#     def calculate_salary(self):
#         print(f'salary of {self.name}: {self.hours*self.rate}')
# name = input()
# hours = int(input())
# rate = int(input())
# e = employee(name,hours,rate)
# e.calculate_salary()

#3
# class book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author
#         self.availability = True
#     def check_out(self):
#         if self.availability:
#             self.availability = False
#             print(f"{self.title} checked out succesfuly")
#         else:
#             print(f"{self.title} not available")
# title = input()
# author = input()
# b = book(title,author)
# b.check_out()

#4
# class account:
#     def __init__(self):
#         self.balance = 0
#     def depositmoney(self,deposit):
#         if deposit >0:
#             self.balance = deposit + self.balance
#         else:
#             print("invalid amount")
#     def withdrawmoney(self,withdraw):
#         if withdraw > self.balance or withdraw<0:
#             print("invalid input")
#         else:
#             self.balance = self.balance - withdraw
#             print(f"remaining balance: {self.balance}")
# deposit = int(input())
# withdraw = int(input())
# a = account()
# a.depositmoney(deposit)
# a.withdrawmoney(withdraw)

#5
# class product:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
# class electronicproduct(product):
#     def __init__(self, name, price,warranty):
#         super().__init__(name, price)
#         self.warranty = warranty
#     def getinfo(self):
#         print(f"{self.name} costs {self.price} with {self.warranty} warranty.")
# name = input()
# price = input()
# warranty = input()
# p1 = electronicproduct(name,price,warranty)
# p1.getinfo()

#6
# class vehicle:
#     def move(self):
#         pass
# class car(vehicle):
#     def move(self):
#         print('car drives on a road')
# class bike(vehicle):
#     def move(self):
#         print('bike rides on road')
# c = car()
# b = bike()
# c.move()
# b.move()

#7
# class menu:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
# class beverages(menu):
#     def __init__(self, name, price,size):
#         super().__init__(name, price)
#         self.size = size
#     def showinfo(self):
#         print(f"{self.name} ({self.size}) - ${self.price}")
# name = input()
# price = input()
# size = input()
# m = beverages(name,price,size)
# m.showinfo()

#8
# class person:
#     def __init__(self,name):
#         self.name = name
# class student(person):
#     def __init__(self, name):
#         super().__init__(name)
#     def describe_role(self):
#         print(f"{self.name} is a student")
# class teacher(person):
#     def __init__(self, name):
#         super().__init__(name)
#     def describe_role(self):
#         print(f"Mrs. {self.name} is a Teacher")
# studentname = input()
# teachername = input()
# s = student(studentname) 
# t = teacher(teachername)
# s.describe_role()
# t.describe_role()

#9
# class user:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email
# class customer(user):
#     def __init__(self, name, email):
#         super().__init__(name, email)
#         self.cart = [] 
#     def additems(self,item,price):
#         self.cart.append(price)
#         print(f"item added to cart: {item}")
#     def checkout(self):
#         print(f"cart total: ${sum(self.cart)}")
# c = customer('ketan','ketan@gamil.com')
# c.additems('maggie',20)
# c.additems("pasta",40)
# c.checkout()

#10
# class appliance:
#     def turn_on(self):
#         pass
#     def turn_off(self):
#         pass
# class fan(appliance):
#     def turn_on(self,speed):
#         print(f"fan turned on at speed {speed}")
#     def turn_off(self):
#         print("fan tuned off")
# class light(appliance):
#     def turn_on(self):
#         print("light turned on")
#     def turn_off(self):
#         print("light tuned off")
# class ac(appliance):
#     def turn_on(self,speed):
#         print(f"ac cooling set to {speed}C")
#     def turn_off(self):
#         print("ac tuned off")
# f = fan()
# l = light()
# a = ac()
# f.turn_on(4)
# f.turn_off()
# l.turn_on()
# l.turn_off()
# a.turn_on(22)
# a.turn_off()