#1
# i=1
# while i<=10:
#     print(i)
#     i+=1

#2
# for i in range(10,0,-1):
#     print(i)

#3
# for i in range(2,51,2):
#     print(i)

#4
# sum=0
# for i in range(1,21):
#     sum=sum+i
# print(sum)

#5
# n= int(input("enter ur number:"))
# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")

#6
# n=int(input("enter ur number:"))
# i=1
# fact=1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)

#7
# n=int(input("enter ur number:"))
# count=0
# while n>0:
#     n=n//10
#     count+=1
# print(count)

#8
# n=int(input("enter ur number:"))
# rev = 0
# while n>0:
#     digit = n%10
#    rev = rev*10 + digit 
#    n= n//10
#print(rev)    

#9
# chars = input("enter ur word:")
# for ch in chars:
#     print(ch)

#10
# n=int(input("enter ur number:"))
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# print(sum)

#11
# for i in range(3):
#     for j in range(3):
#         print("*",end="")
#     print()

#12
# num=1
# for i in range(5):
#     for j in range(5):
#         print(num,end=" ")
#         num+=1
#     print()

#13
# num=65
# for i in range(3):
#     for j in range(3):
#         print(chr(num),end=" ")
#         num+=1
#     print()

#14
# for i in range(2,11):
#     for j in range(1,11):
#         print(f"{i} X {j} ={i*j}")
#     print()

#15
# words = ['apple','Banana','grapes','ORANge']
# vowels ='aeiouAEIOU'
# for word in words:
#     count=0
#     for ch in word:
#         if ch in vowels:
#             count+=1
#     print(f"number of vowels in {word} is {count}")

#16
# for i in range(1,4):
#     for j in range(1,4):
#         print(f"{(i,j)}",end="")
#     print()

#17
# for i in range(5):
#     for j in range(5):
#         print((i+j)%2,end=" ")
#     print(" ")

#18
# a=0
# for i in range(2,51):
#     for j in range(2,i):
#         if i%j==0:
#            a=1
#     if a==0:
#         print(i)
#     a=0

#19
# for i in range(5,51,5):
#     print(i)

#20
# for i in range(100,-1,-10):
#     print(i)

#21
# for i in range(1,100,2):
#     print(i)

#22
# sum=0
# for i in range(1,11):
#     sum=sum+i**2
# print(sum)

#23
# n=int(input("enter ur number:"))
# for i in range(1,n+1):
#     print(i**3,end="")
#     print()

#24
# for i in range(65,91):
#     print(chr(i),end="")
#     print()

#25
# for i in range(10,100):
#     if i % 9==0:
#         print(i)

#26
# for i in range(1,11):
#     if i ==5 :
#         break
#     print(i)

#27
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)

#28
# for i in range(1,6):
#     if i==5:
#         pass
#     else:
#         print(i)

#29
# for i in range(2,21,2):
#     if i==14:
#         break
#     print(i)

#30
# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print(i)

#31
# while True:
#     n=int(input('enter ur number:'))
#     if n==0:
#         break
#     print(f"uhh entered {n}")

#32
# i=2
# count=0
# while True:
#     a=0
#     for j in range(2,i):
#         if i%j==0:
#             a=1
#     if a==0: 
#         print(i)
#         count+=1
#     if count==5:
#         break
#     i+=1

#33
# n=int(input("enter ur number:"))
# for i in range(1,n):
#     pass

#34
# rows=4
# for i in range(1,rows+1):
#     for j in range(i):
#         print("*",end="")
#     print()

#35
# rows =4
# for i in range(rows,0,-1):
#     for j in range(i):
#         print('*',end="")
#     print()

#36
# for i in range(1,5):
#     print(" "*(4-i),end=" ")
#     print("* "*i,end=" ")
#     print()

#37
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

#38
# num=1
# for i in range(1,5):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()

#39
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

#40
# num=65
# for i in range(1,5):
#     for j in range(i):
#         print(chr(num),end=" ")
#         num+=1
#     print()

#41
# for i in range(1,5):
#     for j in range(65,65+i):
#         print(chr(j),end="")
#     print()

#42
# for i in range(1,4):
#     print(" "*(3-i),end=" ")
#     print("* "*((2*i)-1),end=" ")
#     print()

#43
# for i in range(1,4):
#     print(" "*(3-i),end=" ")
#     print("* "*((2*i)-1),end=" ")
#     print()
# for i in range(2,0,-1):
#     print(" "*(3-i),end=" ")
#     print("* "*((2*i)-1),end=" ")
#     print()    

#44
# for i in range(1,6):
#     if i==1 or i==5:
#         print('*'*5,end=" ")
#     else:
#         print("*"+" "*(5-2)+"*",end=" ")
#     print()

#45
# num=1
# for i in range(1,5):
#     print(" "*(4-i),end="")
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()
