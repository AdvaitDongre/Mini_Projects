#password manager 
import random
import string


password = ""
u = string.ascii_lowercase
y = string.ascii_letters
z = string.ascii_uppercase


ch = input("Enter your password: ")

if len(ch) < 7:
    print("Password is weak, here is a new password\n")
    for i in range(5):
        password = password + random.choice(u) + random.choice(string.digits) + random.choice(z) + random.choice(y)
        u,y,z = z,y,u
print(password)