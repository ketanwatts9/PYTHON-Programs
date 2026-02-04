def greet():
    print("hello from module")
if __name__=='__main__':
    print('this file is runs directly')
    greet()
else:
    print('this file is imported as module')