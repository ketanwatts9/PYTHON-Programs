#1
# s = 'ketan'
# count = 0
# for i in s:
#     count+=1
# print(count)

#2
# s = 'ketan'
# r = ""
# for i in range(len(s)-1,-1,-1):
#     r += s[i]
# rev = s[::-1]
# print(rev)
# print(r)

#3
# s = input()
# if s == s[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

#4
# s = input()
# for char in s:
#     print(char)

#5
# s = input().lower()
# count = 0 
# for i in s:
#     if i in 'aeiou':
#         count+=1
#     else:
#         continue
# print(count)

#6
# s = input().lower()
# vowels = 0
# consonats = 0
# digit = 0
# spaces = 0 
# for i in s:
#     if i.isalpha():
#         if i in 'aeiou':
#             vowels += 1
#         else:
#             consonats += 1
#     elif i.isdigit():
#         digit+=1
#     elif i.isspace():
#         spaces += 1
# print("vowels: ",vowels)
# print("consonants: ",consonats)
# print("digits: ",digit)
# print("spaces: ",spaces)

#7
# s = input()
# new = ''
# for i in s:
#     new += chr(ord(i)-32)
# print(new)

#8
# s = input()
# result = ""
# for i in s:
#     if i.isspace():
#         continue
#     else:
#         result+=i
# print(result)

#9
# s = input()
# new = s.split()
# count = len(new)
# print(count)

#10
# s = input()
# visited = ""
# for char in s:
#     if char not in visited:
#         print(char,':', s.count(char))
#         visited += char

#11
# s = input()
# visited = ''
# for i in s:
#     if i not in visited:
#         print(i)
#         break
#     else:
#         visited +=i

#12
# s = input()
# visited =""
# for i in s:
#     if i in visited:
#         continue
#     else:
#         visited+=i
# print(visited)

#13
# s1 = input()
# s2 = input()
# if sorted(s1) == sorted(s2):
#     print('anagrams')
# else:
#     print('not anagrams')  

#14
# s = input()
# digit = ''
# other = ''
# for i in s:
#     if i.isdigit():
#         digit += i
#     else:
#         other += i
# if other == "":
#     print('it contains only digits')
# else:
#     print('contains other than digit')

#15
# s = input()
# mylist = s.split()
# maximum = max(sorted(mylist))
# print(maximum)

#16
# s = input()
# result = ''
# for word in s.split():
#     new = word[::-1]+" "
#     result += new
# print(result)

#17
# s = input()
# print(s.title())

#18
# vowels = 'aeiou'
# new  = ''
# s= input()
# for char in s:
#     if char in vowels:
#         new += '*'
#     else:
#         new += char
# print(new)

#19
# s = input()
# substring = input()
# if substring in s:
#     print('yes')
# else:
#     print('no')

#20
# s = input()
# substing = input()
# print(s.count(substing))

#21
# s = input()
# for i in range(len(s)):
#     if i%2==0:
#         print(s[i],end="")
#     else:
#         continue

#22
# s = input()
# for char in s:
#     if char.isdigit():
#         print(char,end="")

#23
# s = input()
# upper = 0
# lower = 0
# for char in s:
#     if char.isupper():
#         upper += 1
#     elif char.islower():
#         lower +=1
# print("upper:",upper)
# print("lower:",lower)

#24
# s = input()
# new = s[-1] + s[1:-1] +s[0] 
# print(new)   