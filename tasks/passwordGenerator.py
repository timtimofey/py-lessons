import random
chars = '12345fghgfhklgjhirteop[werkdf'
num = int(input("кол-во паролей: "))
length = int(input())
for n in range(num):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    print(password)