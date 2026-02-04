#1
# my_dict = {'ketan':90,"abc":34}
# print(my_dict)

#2
# my_dict = {'ketan':90,"abc":34,"aaaaaa":23}
# print(max(my_dict))

#3
# s = 'ketannnnn'
# mydict = {i: s.count(i) for i in s}
# print(mydict)

#4
# a = {'ketan':34}
# b = {'abc':36}
# a.update(b)
# print('marged:',a)

#5
# a = {'ketan':34,'abc':463}
# if 'abc' in a:
#     print('yes')
# else:
#     print('no')

#6
# a = {'ketan':56,'abc':45}
# b = a.keys()
# for key in b:
#     print(key)
# c = a.values()
# for values in c:
#     print(values)

#7
# a = {'ketan':56,'abc':45}
# del a['abc']
# print(a)

#8
# n = int(input())
# a = {x:x*x for x in range(1,n+1)}
# print(a)

#9
# a = {'ketan':23,'abc':45}
# sum = 0  
# value = a.values()
# for i in value:
#     sum += i
# print(sum)

#10
# key = ['a','b','c']
# value = [12,12,43]
# a = {keys:values for keys,values in zip(key,value)}
# print(a)

#11
# a = {'ketan':23,'abc':54}
# b = sorted(a.items())
# print(dict(b))

#12
# a = {'ketan':23,'abc':87}
# print(dict(sorted(a.items())))

#13
# a = {'ketan':23,'abc':87}
# count = 0 
# for i in a:
#     count += 1
# print(count)

#14
# a = {'ketan':12,'abc':3}
# for i in a:
#     a[i] = a[i]**2
# print(a)

#15
# a = (('ketan',23),('abc',43))
# print(dict(a))

#16
# n = int(input())
# a = {i:i**3 for i in range(1,n+1)}
# print(a)