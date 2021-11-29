""""
number = 10
number += 5
print(number)


num1 = 5
num1 *= 2
print(num1)


first_num = "2"
second_num = 9
third_num = first_num + second_num
print(third_num)


a = 50
b = 6
result = 5 == 5
print(result)

print(a != b)
print(a > b)
print(a < b)


bool1 = True
bool2 = False
print(bool1 != bool2)


age = 18
weight = 57
result = age > 21 or weight == 58
print(result)


name = "Tom"
surname = 'Smith'
fullname = name + " " + surname
print(fullname)


print("привет\n валера")
print("привет\"валера\"")


age = 18
if age >= 21:
    print("Доступ разрешен")
elif age >= 18:
    print("Доступ частично разрешён")
else:
    print("Доступ запрещен")
print("завершение работы")
"""

age = 50
if age >= 18:
    print("Больше 17")
    if age > 21:
        print("Больше 21")
    else:
        print("От 18 до 21")
