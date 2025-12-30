import random
import string

print("----Password Generator----")

length=int(input("Enter password length:"))

use_upper=input("Include uppercase letters(y/n):").lower()
use_lower=input("Include lowercase letters(y/n):").lower()
use_digits=input("Include digits?(y/n):").lower()
use_symbols=input("Include special characters?(y/n):").lower()

selected_sets = []
all_characters = ""

if use_upper=='y':
    selected_sets.append(string.ascii_uppercase)
    all_characters += string.ascii_uppercase

if use_lower=='y':
    selected_sets.append(string.ascii_lowercase)
    all_characters+=string.ascii_lowercase

if use_digits=='y':
    selected_sets.append(string.digits)
    all_characters+=string.digits

if use_symbols=='y':
    selected_sets.append(string.punctuation)
    all_characters+=string.punctuation

if not all_characters:
    print("Error:select at least one complexity option.")
    exit()

if length<len(selected_sets):
    print("Error:password length too short for selected complexity")

password_chars=[random.choice(s) for s in selected_sets]

remaining_length=length-len(password_chars)
password_chars+=random.sample(all_characters,remaining_length)

random.shuffle(password_chars)
password="".join(password_chars)

if length>=9 and len(selected_sets)>=3:
    strength = "strong"
elif length >= 8:
    strength="Medium"
else:
    strength="week"

print("\nGenerated password:",password)
print("Password strength:",strength)