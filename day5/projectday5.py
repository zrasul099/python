import random
from random import shuffle

letters = ['a','b','c','d','e','f','g','j','h','k','l','m','n','o','p','r','t','u','v','w','A','B','C','D','E','F','G','H','K']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&']




print("Wellcome to password generator")
nr_letter = int(input("how many letters would you like in you password?"))
nr_symbols = int(input("how many symbols would you like in your password?"))
nr_numbers = int(input("how many numbers would you like in your password"))
all_password = nr_numbers + nr_symbols +nr_letter


password = ""
for char in range(1,nr_letter+1):
    password+= random.choice(letters)

for char in range(1,nr_numbers+1):
    password+=random.choice(numbers)


for char in range(1,nr_symbols+1):
    password+=random.choice(symbols)

print(password)


password_list = []
for char in range(0,nr_letter):
    password_list.append(random.choice(letters))
for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))
for char in range(0,nr_numbers):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)
password2 = ""
for char in password_list:
    password2+= char
print(password2)