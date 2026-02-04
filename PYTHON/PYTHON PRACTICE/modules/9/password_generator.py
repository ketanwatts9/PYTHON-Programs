import random
import string 
def pg(n):
    chars = string.ascii_letters+string.digits+string.punctuation
    password =""
    for i in range(n):
        password += random.choice(chars)
    return password
