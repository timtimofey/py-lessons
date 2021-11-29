""" закомментировать код
choice = "y" основной способ получения случайного значения из списка

while choice.lower() == "y":
    print("Привет")
    choice = input("Y чтобы продолжить")
print("Программа завершена")


num = int(input("Введите число: "))
i = 1
fact = 1
while i <= num:
    fact *= i
    i += 1
print("Факториал числа", num, "равен", fact)


num = int(input("Введите число: "))
fact = 1
for i in range(1, num+1): ВЫПОЛНИТЬ ДЕЙСТВИЕ ОПРЕДЕЛЕННОЕ КОЛ-ВО РАЗ
    fact *= i
print("Факториал числа", num, "равен", fact)


for i in range(1,5) :
    for j in range (1,12):
        print(i * j, end="\t")
    print("\n")

print("Для выходу нажмите Y")

while True:
    data = input("Введите сумму для обмена: ")
    if data.lower() == "y" :
        break #выход из цикла
    money = int(data)
    cache = round(money / 74)
    print("К выдаче", cache,"долларов")
print("Работа завершена")
"""

print("Для выхода нажмите Y")

while True:
    data = input("Введите сумму для обмена: ")
    if data.lower() == "y" : #нижний регистр
        break #выход из цикла
    money = int(data)
    if money <0:
        print("Сумма должна быть положительная")
        continue
    cache = round(money / 74)
    print("К выдаче", cache,"долларов")
print("Работа завершена")