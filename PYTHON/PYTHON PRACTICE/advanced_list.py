#1
# n = int(input())
# mylist = [i*i for i in range(1,n+1)]
# print(mylist)

#2
# list1 = [1,2,3,4,5,6,7,8]
# mylist = [i for i in list1 if i%2==0]
# print(mylist)

#3
# cel = [1,2,3,4,5]
# f = [(1.8*c)+32 for c in cel]
# print(f)

#4
# mylist = [(n,n*n*n) for n in range(1,11)]
# print(mylist)

#5
# list1 = ['ketan', 'apple', 'boy', 'orange']
# mylist =  [s for s in list1 if s[0] in 'aeiou']
# print(mylist)

#6
# list1 = [1,-2,3,4,-7,3,-98,0,-4,-2]
# mylist = ['positive' if i>0 else 'negative' for i in list1]
# print(mylist)

#7
# list1 = [[1,2,3], [4,5], [6,7,8,9]]
# mylist = [item for sublist in list1 for item in sublist]
# print(mylist)

#8
# list1= [1,-2,-3,5,-8,-7]
# mylist= [0 if i<0 else i for i in list1]
# print(mylist)

#9
# list1 = ['ketan','what','good','my']
# mylist = [len(i) for i in list1]
# print(mylist)

#10
# mylist = [i for i in range(1,101) if i%3==0 and i%5==0]
# print(mylist)

#11
# a = 'ketan'
# mylist = [i.upper() for i in a]
# print(mylist)

#12
# list1 = [1,2,4,1,3,1,1,3,4,4,2,1,3,1,5]
# mylist = []
# [mylist.append(i) for i in list1 if i not in mylist] 
# print(mylist)

#13
# def square(n):
#     return n*n
# list1 = [1,2,3,4,5]
# print(list(map(square,list1)))

#14
# def upper(s):
#     return s.upper()
# list1 = ['ketan','watts','absd','what']
# mylist = list(map(upper,list1))
# print(mylist)

#15
# list1 = [1,2,3,4,2,1,3,1,1]
# list2 = [1,2,3,1,2,1,2,3,1]
# print(list(map(lambda a,b:a+b,list1,list2)))

#16
# list1 = [1.0,1.4,5.6,2.8]
# print(list(map(int,list1)))\

#17
# def palindrome(s):
#     if s[::-1] == s:
#         return s
# list1 = ['ketan','mam','abcba','what']
# print(list(filter(palindrome,list1)))

#18
# def positive(n):
#     if n>0:
#         return n
# list1 = [1,-1,3,2,-2]
# print(list(filter(positive,list1)))

#19
# def prime(n):
    # if n <= 1:
    #     return False
    # if n == 2:
    #     return True
    # if n % 2 == 0:
    #     return False
    
    # for i in range(3, int(n**0.5) + 1, 2):
    #     if n % i == 0:
    #         return False
    # return True
# list1 = [1,3,5,6,4,2,1,4,7,54,6]
# print(list(filter(prime,list1)))

#20
# def more(s):
#     if len(s)>5:
#         return s
# list1 = ['ketanwatts','what','mam']
# print(list(filter(more,list1)))

#21
# from functools import reduce
# list1= [1,2,2,1,2,33,14,5,32,6,543,838,3]
# print(reduce(lambda x,y:x if x>y else y,list1))

#22
# from functools import reduce
# list1 = [1,4,2,13,4,321,32,3223,32,3,42]
# print(reduce(lambda x,y: x*y,list1))

#23
# from functools import reduce
# list1 = [1,2,23,2,56,3,4,35,2,2,3,325,353,2222,32]
# even = [i for i in list1 if i%2==0]
# print(reduce(lambda x,y: x+y,even))

#24
# from functools import reduce
# list1 = ['ketan','watts']
# print(reduce(lambda x,y:x+y,list1))

#25
# r = int(input())
# c = int(input())
# num = 0
# for i in range(r):
#     for j in range(c):
#         print(num,end=' ')
#     print()

#26
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# for row in matrix:
    # for element in row:
        # print(element,end=' ')
    # print() 

#27
# matrix = eval(input())
# sum_of_row = []
# for row in matrix:
#     a = sum(row)
#     sum_of_row.append(a)
# print(sum_of_row)

#28
# matrix = eval(input())
# col_sum = [sum(i) for i in zip(*matrix)]
# print(col_sum)

#29
# matrix = eval(input())
# elements = []
# for row in matrix:
#     for element in row:
#         elements.append(element)
# print(max(elements))

#30
# matrix = eval(input())
# element = int(input())
# found = False
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j]==element:
#             print(f'element is at [{i}][{j}]')
#             found = True
#             break
#         if found:
#             break
# if not found:
#     print('not found')
        
#31
#A
# matrix = eval(input())
# rows = len(matrix)
# cols = len(matrix[0])
# transpose = []
# for j in range(cols):
#     row = []
#     for i in range(rows):
#         row.append(matrix[i][j])
#     transpose.append(row)
# print(transpose)

#B
# matrix = eval(input())
# transpose = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
# print(transpose)

#32
# r = int(input())
# c = int(input())
# matrix = []
# for i in range(r):
#     row = list(map(int,input().split()))
#     matrix.append(row)
# for i in range(r):
#     for j in range(c):
#         if i == 0 or i == r-1 or j==0 or j == c-1:
#             print(matrix[i][j],end=" ") 

#33
# r = int(input())
# c = int(input())
# matrix = []
# for i in range(r):
#     row = list(map(int,input().split()))
#     matrix.append(row)
# for i in range(r):
#     print('primary:',matrix[i][i])
# for i in range(r):
#     print('secondary: ',matrix[i][c-i-1])

#34
# matrix = eval(input())
# count = 0
# for row in matrix:
#     for element in row:
#         if element > 50 :
#             count += 1
# print(count)
         
#35
# A = eval(input())
# B = eval(input())
# matrix = []
# for i in range(len(A)):
#     row = []
#     for j in range(len(A[i])):
#         sum = A[i][j] + B[i][j]
#         row.append(sum) 
#     matrix.append(row)
# print(matrix)

#36
# A = eval(input())
# B = eval(input())
# result = [[0 for j in range(len(B[0]))] for i in range(len(A))]
# for i in range(len(A)):
#     for j in range(len(B[0])):
#         for k in range(len(B)):
#             result[i][j] += A[i][k]*B[k][j]
# print(result)

#37
# matrix = eval(input())
# elements = []
# for row in matrix:
#     for element in row:
#         elements.append(element)
# print(elements)

#38
# matrix = eval(input())
# for row in matrix:
#     for element in row:
#         if element<0:
#             print(0,end=' ')
#         else:
#             print(element,end=' ')
#     print()

#39
# jagged = [[1,2,3], [4,5], [6,7,8,9]]
# for row in jagged:
    # for element in row:
        # print(element,end = ' ')
    # print()

#40
# r = int(input())
# jagged = []
# for sublist in range(r):
    # c = int(input())
    # sublist = list(map(int,input().split()))
    # jagged.append(sublist)
# print(jagged)
# for sublist in jagged:
    # for element in sublist:
        # print(element,end=' ')
    # print()

#41
# jagged = eval(input())
# lenghth_list = list(map(len,jagged))
# print(max(lenghth_list))

#42
# def prime(n):
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 return 'prime'
#                 break
#         else:
#             return 'not prime'
#     else:
#         return 'not prime'
# jagged = eval(input())
# count = 0
# for row in jagged:
#     for element in row:
#         if prime(element) == "prime":
#             count+=1
# print(count)

#43
# jagged = eval(input())
# row_sum = []
# for row in jagged:
#     row_sum.append(sum(row))
# print(row_sum)

#44
# jagged = eval(input())
# elements = []
# for row in jagged:
#     for element in row:
#         elements.append(element)
# print(elements)

#45
# jagged = eval(input())
# flatten = [element for row in jagged for element in row]
# print(flatten)

#46
# jagged = eval(input())
# for row in jagged:
#     for element in row:
#         if element>100:
#             print(100,end=" ")
#         else:
#             print(element,end=" ")
#     print()