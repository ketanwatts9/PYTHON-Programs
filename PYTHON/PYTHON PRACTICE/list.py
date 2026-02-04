#1
# mylist = list(map(int,input().split()))
# max_num = mylist[0]
# min_num = mylist[0]
# for i in mylist:
#     if i > max_num:
#         max_num = i
#     elif i < min_num:
#         min_num = i
# print('maximum number from list: ',max_num)
# print('minimum number from list: ',min_num)

#2
# mylist = list(map(int,input().split()))
# print("your list: ",mylist)
# rvrsd = []
# for i in range(len(mylist)-1,-1,-1):
#     rvrsd.append(mylist[i])
# print('reversed list: ',rvrsd)

#3
# mylist = list(map(int,input().split()))
# print(mylist)
# element = int(input("enter number u want to count: "))
# count = 0
# for i in mylist:
#     if i == element:
#         count += 1
# if count == 0:
#     print('element not found')
# else:
#     print(count)

#4
# mylist = list(map(int,input().split()))
# largest = max(mylist)
# second = None
# for num in mylist:
#     if num != largest:
#         if second is None or num > second:
#             second = num
# print(second)

#5
# mylist = list(map(int,input().split()))
# odd = []
# even = []
# for i in mylist:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("odd numbers: ",odd)
# print("even  numbers: ",even)        

#6
# mylist = input().split()
# print("your list: ",mylist)
# element = input("enter element u want to remove: ")
# newlist = []
# for i in mylist:
#     if i != element:
#         newlist.append(i)
# print('your updated list: ',newlist)

#7
# mylist = input().split()
# print("your list: ",mylist)
# newlist = mylist[::-1]
# if mylist == newlist:
#     print('its palindrome')
# else:
#     print('not a palindrome')

#8
# mylist = list(map(int,input().split()))
# print("your list: ",mylist)
# even_sum = 0
# odd_sum = 0
# for i in mylist:
#     if i in mylist[::2]:
#         even_sum += i
#     else:
#         odd_sum += i
# print("sum at even indexes: ",even_sum)
# print("sum at odd indexes: ",odd_sum) 

#9
# mylist = list(map(int,input().split()))
# print("your list: ",mylist)
# a = int(input("enter starting position: "))
# b = int(input("enter ending position: "))
# print('required: ',mylist[a-1:b])

#10
# mylist = list(map(int,input().split()))
# element = int(input("enter element whose index is u want to find: "))
# pos = -1
# for i in range(len(mylist)):
#     if mylist[i] == element:
#         pos = i
# if element not in mylist:
#     print("not found")
# else:
#     print(pos)

#11
# mylist = list(map(int,input().split()))
# k = int(input("give k: "))
# for i in range(k):
#     a = mylist[0]
#     mylist.remove(mylist[0])
#     mylist.append(a)
# print(mylist)

#12
# mylist = list(map(int,input().split()))
# new = []
# for i in range(len(mylist)):
#     if i % 2 == 0:
#         new.append(mylist[i]) 
# print(new)

#13
# mylist = list(map(int,input().split()))
# first = []
# second = []
# for i in range(len(mylist)):
#     if i < len(mylist)//2:
#         first.append(mylist[i])
#     else: 
#         second.append(mylist[i])
# print(first)
# print(second)

#14
# mylist = list(map(int,input().split()))
# new = []
# idx = int(input("enter at which index u want to insert: "))
# element = int(input("enter element u want to insert: "))
# for i in range(len(mylist)+1):
#     if i < idx:
#         new.append(mylist[i])
#     elif i == idx:
#         new.append(element)
#     else:
#         new.append(mylist[i-1])
# print(new)

#15
# mylist = list(map(int,input().split()))
# new = []
# idx = int(input("enter at which index u want to remove: "))
# for i in range(len(mylist)):
#     if i == idx:
#         continue
#     else:
#         new.append(mylist[i])
# print(new)

#16
# mylist = list(map(int,input().split()))
# list1 = []
# list2 = []
# for i in range(len(mylist)):
#     if i<(len(mylist)//2):
#         list2.append(mylist[i])
#     else:
#         list1.append(mylist[i])
# print(list1+list2)

#17
# mylist = list(map(int,input().split()))
# neg = []
# pos = []
# for i in mylist:
#     if i<0:
#         neg.append(i)
#     else:
#         pos.append(i)
# print(neg+pos)

#18
# mylist = list(map(int,input().split()))
# zero = []
# baki = []
# for i in mylist:
#     if i == 0:
#         zero.append(i)
#     else:
#         baki.append(i)
# print(baki+zero)

#19
# mylist = list(map(int,input().split()))
# count = 0 
# avg = sum(mylist)/len(mylist)
# for i in mylist:
#     if i > avg:
#         count+=1
# print(count)

#20
# arr = [1,4,2,4,3,5,8,7]
# for i in range(len(arr)):
#     for j in range(len(arr)-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# print(arr)

#21
# arr = ['ketan','apple','mango','cat']
# for i in range(len(arr)):
#     for j in range(len(arr)-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# print(arr)

#22
# arr1 = [1,2,3,4,5]
# arr2 = [1,3,4,5,6]
# arr = arr1+arr2
# for i in range(len(arr)):
#     for j in range(len(arr)-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# print(arr)

#23
# arr = [1,2,2,1,1,1,2,4,6,7,0,8,9,]
# arr1 = []
# for i in arr:
#     if i not in arr1:
#         arr1.append(i)
# print(arr1)

#24
# arr = [1,2,3,4,5,6,7,8,9]
# target = int(input("enter ur target: "))
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]+arr[j]==target:
#             print(f"({arr[i]},{arr[j]})")

#25
# arr = [1,2,2,3,4,5,6,7,78,8]
# for i in range(len(arr)):
#     count = 1
#     if arr[i] != -1:
#         for j in range(i+1,len(arr)):
#             if arr[i] == arr[j]:
#                 count+=1
#                 arr[j] = -1
#         print(arr[i], '=', count)

#26
# list1 = [1,2,3,4]
# list2 = [2,3,4,5]
# for i in range(len(list1)-1,-1,-1):
#         if list1[i] in list2:
#             list1.remove(list1[i])
# print(list1)

#27
# arr = [1,2,[1,4,3,[5,6],1,[3,5,6,[0]]]]
# def nested(arr):
#     new = []
#     for i in arr:
#         if isinstance(i,list):
#             new.extend(nested(i))
#         else:
#             new.append(i)
#     return new
# print(nested(arr))

#28
# arr = [1,2,3,4,5,6,7,8,9]
# k = int(input("enter number: "))
# size = len(arr)//k
# parts = []
# i = 0
# while i<len(arr):
#     parts.append(arr[i:i+size])
#     i+=size
# print(parts)

#29
# arr = [1,1,2,3,4,3,2,1,2,3,5,2,6,4,3]
# max_element = arr[0]
# maxcount = 0
# for i in arr:
#     count = arr.count(i) 
#     if count>maxcount:
#         maxcount= count
#         max_element=arr[i]
# print(max_element,'=',maxcount)

#30
# lst1 = [1,2,3]
# lst2 = [1,2,3]
# if len(lst1) != len(lst2):
#     print('not equal')
# else:
#     equal = True
#     for i in range(len(lst1)):
#         if lst1[i] != lst2[i]:
#             equal = False
#             break
# if equal == True:
#     print('equal')
# else:
#     print('not equal')    