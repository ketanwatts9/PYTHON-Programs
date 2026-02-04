#1
# def add_num(a,b):
#     return a+b
# print(add_num(5,2))
# print(add_num(b=2,a=1))

#2
# def square(n):
#     return n*n
# print(square(2))

#3
# def odd_even(n):
#     if n%2==0:
        # print("even")
    # else:
        # print("odd")
# odd_even(2)
# def odd_even(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
# print(odd_even(2))

#4
# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact*i
#     return fact
# print(factorial(3))

#5
# def largest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c:
#         return b
#     else:
#         return c
# print(largest(-222,222,2121))

#6
# def count(word):
#     count = 0
#     vowel = 'aeiouAEIOU' 
#     for i in word:
#         if i in vowel:
#             count = count+1
#     print(count)
# word = input()
# count(word)

#7
# def sum_of_digits(x):
#     sum = 0
#     while x>0:
#         n = x % 10
#         sum = sum + n
#         x = x // 10
#     return sum
# print(sum_of_digits(12))
# print(sum_of_digits(233))

#8
# def table(n):
#     for i in range(1,11):
#         print(f"{n} X {i} = {n*i}")
# table(5)

#9
# def cel_to_fahrnheit(c):
#     f = (1.8*c)+32
#     return f
# print(cel_to_fahrnheit(0))

#10
# def palindrome(my_string):
#     if my_string == my_string[::-1]:
#         return "yes its a palindrome"
#     else:
#         return "no its not a palindrome"
# print(palindrome("ketan"))
# print(palindrome("mam"))

#11
# def simple_interest(p,r,t):
#     return (p*r*t)/100
# print(simple_interest(100,1,1))

#12
# def student_details(name,age,grade):
#     print(f"name = {name} age = {age} grade = {grade}")
# student_details(name="ketan",age=18,grade="A")

#13
# def power(base,power=2):
#     print(base**power)
# power(2)
# power(6)

#14
# def sum_of_numbers(*numbers):
#     total = 0
#     for i in numbers:
#         total = total + i
#     print(total)
# sum_of_numbers(1,2,3,4)

#15
# def max_of_elements(*numbers):
#     return max(numbers)
# print(max_of_elements(1,2,3,45,665,56543))

#16
# def show_info(**person):
#     for key,value in person.items():
#         print(f"{key} : {value}")
# show_info(name = "ketan", age = 18, grade = "A")

#17
# def info(name,age=18):
#     print(f"name={name},age={age}")
# info("ketan")
# info("watts",21)

#18
# def info(*numbers,**person):
#     print(numbers)
#     print(person)
# info(1,2,3,name='ketan',age=18,uni='chitkara',year=2025)

#19
# x = 5 #global variable
# def demo():
#     x = 10 #local varialble
#     print("local x =",x)
# demo() 
# print('global x =',x)

#20
# counter = 0
# def update():
#     global counter
#     counter += 1
# update()
# update()
# print('counter =',counter)

#21
# my_list = [1,2,3]
# def update():
#     global my_list
#     my_list.append(4)
# print('list before update =',my_list)
# update()
# print('list after update =',my_list)

#22
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n*fact(n-1)
# print(fact(2))
# print(fact(5))

#23
# def sum_of_n(n):
#     if n == 1:
#         return 1
#     return n + sum_of_n(n-1)
# print(sum_of_n(1))
# print(sum_of_n(2))

#24
# def print_num(n):
#     if n == 0:
#         return
#     print_num(n-1)
#     print(n)
# print_num(5)

#25 
# def print_reverse(n):
#     if n == 0:
#         return
#     print(n)
#     print_reverse(n-1)
# print_reverse(5)

#26
# def fab(n,a=0,b=1):
#     if n == 0:
#         return
#     print(a, end=" ")
#     fab(n-1, b, a+b)
# fab(10)

#27
# def rvrs(s):
#     if s == '':
#         return ''
#     return rvrs(s[1:]) + s[0]
# print(rvrs('ketan'))

#28
# def gcd(a,b):
#     if b == 0:
#         return a
#     return gcd(b,a%b)
# print(gcd(1,2))
# print(gcd(12,48))

#29
# def count_digit(n):
#     if n == 0:
#         return 0
#     return 1 + count_digit(n//10)    
# print(count_digit(123))

#30
# def sum_digit(n):
#     if n == 0:
#         return 0
#     return n % 10 + sum_digit(n//10)
# print(sum_digit(12))

#31
# def power(base, sir):
#     if sir == 0:
#         return 1
#     return base * power(base ,sir-1)
# print(power(2,2))

#32
# def palindrome(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return palindrome(s[1:-1])
# print(palindrome("madam"))
# print(palindrome("ketan"))

#33
# def min_list(mylist):
#     if len(mylist) == 1:
#         return mylist[0]
#     return min(mylist[0], min_list(mylist[1:]))
# mylist = [1,2,4,5,54,432,5,3,4625,3252]
# print(min_list(mylist))

#34
# def max_list(mylist):
#     if len(mylist) == 1:
#         return mylist[0]
#     return max(mylist[0], max_list(mylist[1:]))
# mylist = [1,2,4,5,54,432,5,3,4625,3252]
# print(max_list(mylist))

#35
# def poduct_list(mylist):
#     if len(mylist) == 1:
#         return mylist[0]
#     return mylist[0]*poduct_list(mylist[1:])
# print(poduct_list([1,2,34]))

#36
# add = lambda a,b: a+b
# print(add(1,2))

#37
# square = lambda x: x**2
# print(square(2))

#38
# odd_even = lambda x: "even" if x%2==0 else "odd"
# print(odd_even(2))

#39
# greater = lambda a,b: a if a>b else b
# print(greater(1,2))

#40
# def fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact*i
#     return fact
# n = int(input("enter n: "))
# r = int(input("enter r: "))
# nCr = fact(n) / (fact(n-r)*fact(r))
# print(nCr)

#41
# def remove(s):
#     if s == '':
#         return ''
#     rest = remove(s[1:])
#     if s[0] in rest:
#         return rest
#     else:
#         return s[0] + rest
# print(remove('ketan'))
# print(remove('aabbwygeadw'))

#42
# def issorted(mylist):
#     if len(mylist) == 1:
#         return True
#     return mylist[0] <= mylist[1] and issorted(mylist[1:])
# print(issorted([1,2,3]))
# print(issorted([327,32829,232]))

#43
# def index(mylist, x):
#     if not mylist:
#         return -1
#     if mylist[0] == x:
#         return 0
#     idx = index(mylist[1:],x)
#     return -1 if idx == -1 else idx+1
# print(index([1,2,3,4,5,6,7,7],7))

#44
# def freq(word):
#     if not word:
#         return {}
#     rest = freq(word[1:])
#     w = word[0]
#     rest[w] = rest.get(w,0) + 1
#     return rest 
# para = "python is powerful and wonderful language and it is very easy to learn"
# word = para.split()
# print(freq(word))