#Jonathan Contreras
#AP Computer Science
#B1


import random

regularChars = "abcdefghijklmnopqrstuvwxyz123467890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
specialChars = "!@#$%^&*()"

number = input("Number of passwords? ")
number = int(number)

length = input("How many character long do you want your password? ")
length = int(length)

specialCharacters = input("Do you want special characters in your password? (1 for 'yes' 2 for 'no') ")
specialCharacters = int(specialCharacters)

if specialCharacters == 1:
    
    for p in range (number):
        password = ''
        for c in range(length):
            password = random.choice(regularChars)
            password += random.choice(specialChars)
        print(password)
    
elif specialCharacters == 2:

    for p in range (number):
        password = ''
        for c in range(length):
            password += random.choice(regularChars)
        print(password)



