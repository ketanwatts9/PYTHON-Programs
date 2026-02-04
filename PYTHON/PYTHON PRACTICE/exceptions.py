#1 
# try:
#     a = int(input())
#     b = int(input())
#     result = a/b
#     print(result)
# except ZeroDivisionError:
#     print("division by zero is not allowed")
# except ValueError:
#     print("invalid input")

#2
# try:
#     file = input()
#     with open(f"{file}","r") as f:
#         c = f.read()
#         print(c)
# except FileNotFoundError:
#     print("file not found")

#3
# count = 0
# total = 0
# for i in range(3):
#     try:
#         marks = int(input())
#         total += marks
#         count += 1 
#     except ValueError:
#         print("invalid input skipped")
# if count>0:
#     print("average marks:",total/count)

#4
# class InsuffientFundsError(Exception):
#     pass
# try:
#     balance = int(input())
#     withdraw = int(input())
#     if balance < withdraw:
#         raise InsuffientFundsError("insufficient funds!")
#     balance -= withdraw
#     print(balance)
# except InsuffientFundsError as e:
#     print(e)

#5
# class InvalidAgeError(Exception):
#     pass
# try:
#     age = int(input())
#     if age<0:
#         raise ValueError
#     if age<5 or age>18:
#         raise InvalidAgeError
#     else:
#         print("age is valid")
# except InvalidAgeError:
#     print("invalid age entered")
# except ValueError:
#     print("invalid age")

#6
# try:
#     with open("product.txt","r") as f:
#         for line in f:
#             price = int(price)
#             print(price)
# except FileNotFoundError:
#     print("file not found")
# except ValueError:
#     print("malformed data in file")

#7
# class OverheatError(Exception):
#     pass
# try:
#     temp = int(input())
#     if temp > 100:
#         raise OverheatError
#     else:
#         print("temperature is okkk")
# except OverheatError:
#     print("Warning: Overheat detected!")
# finally:
#     print("System monitoring complete")

#8
# try:
#     a = int(input())
#     b = int(input())
#     result = a/b
#     print(result)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)

#9
# class NegativeTransactionError(Exception):
#     pass
# try:
#     with open("myfile.txt","r") as f:
#         for line in f:
#             try :
#                 name,amnt = line.strip().split(",")
#                 a = int(amnt)
#                 if a<0:
#                     raise NegativeTransactionError
#                 print(f"{name} = {amnt}")
#             except NegativeTransactionError:
#                 print(f"Error: NegativeTransactionError for {name}")
#             except ValueError:
#                 print(f"Error: Invalid amount for {name}")
# except FileNotFoundError:
#     print("Error: file not found")

#10
# class LocalFileMissingError(Exception):
#     pass
# class ServerTimeoutError(Exception):
#     pass
# files = ["report.txt","summary.txt","data.txt"]
# try:
#     for file in files:
#         try:
#             if file == "summary.txt":
#                 raise LocalFileMissingError
#             if file == 'data.txt':
#                 raise ServerTimeoutError
#             print(f"Uploaded: {file}")
#         except LocalFileMissingError:
#             print("Error: LocalFileMissingError for summary.txt")
#         except ServerTimeoutError:
#             print("Error: ServerTimeoutError - retry later")
# except:
#     print("Unexpected Error Occured")