import random
import string 

print("----Password Generator----")

length=int(input("Enter the desired password length:"))

char=string.ascii_letters + string.digits + string.punctuation

password=""
for i in range(length):
    password = password +random.choice(char)

print("Generated password:",password)
