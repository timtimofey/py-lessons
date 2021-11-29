"""
создание функции
def say_hello():
    print("hello")


say_hello()
say_hello()


ФУНКЦИЯ С ПАРАМЕТРОМ
def say_hello(name):
    print("hello,",name)


say_hello("Tom")
say_hello("Bob")



Функция со стандартным значением
def say_hello(name = "Tom"):
    print("hello,",name)


say_hello()
say_hello("Bob")



неопр кол-во параметров
def sum(*params):
    result = 0
    for n in params:
        result += n
    return result


sum_num1 = sum(1, 2, 3, 4, 5, 54, 4353)
sum_num2 = sum(3, 4, 5, 6)
print(sum_num1)
print(sum_num2)


возвращение результата
def exchange (usd_rate,money):
    result = round(money/usd_rate, 2)
    return result


result1 = exchange(60, 30000)
print(result1)
result2 = exchange(72, 50324)
print(result2)



вызов главной функции
def main():
    say_hello("Tom")
    usd_rate = 73
    money = 30000
    result = exchange(usd_rate, money)
    print("К выдаче", result, "долларов")



def exchange (usd_rate,money):
    result = round(money/usd_rate, 2)
    return result


def say_hello(name):
    print("hell,", name )

main()



видимость переменных
name = "Tom"

def say_hi():
    print("hello" , name)

def say_bye():
    name = "Bob"
    print("Good bye", name)

def main():
    say_bye()
    say_hi()
main()
"""