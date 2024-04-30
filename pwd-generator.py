import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(,)','*','+']

print("WELCOME TO PASSWORD GENERATOR")

n_letters=int(input("How Many Letters you want in your Password?\n"))
n_numbers=int(input("How Many Numbers you want in your Password?\n"))
n_symbols=int(input("How Many Symbols you want in your Password?\n"))

password_list=[]

for i in range(1,n_letters+1):
    char =random.choice(letters)
    password_list += char

for i in range(1,n_numbers+1):
    char = random.choice(numbers)  
    password_list += char

for i in range(1,n_symbols+1):
    char =  random.choice(symbols)    
    password_list += char

print(password_list)  
random.shuffle(password_list)
print(password_list)  
password=""
for char in password_list:
    password += char

print("Your Password Is:-",password)
