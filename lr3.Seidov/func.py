import random

def get_random_num():
    """Возврат рандомного числа в диапазоне"""
    rnd_num = random.randint(0, 100)
    return rnd_num

def print_happy_birthday(age, name):
    """Вывод в консоль поздравления с днем рождения"""
    print(f"Поздравляю с {age}-летием, {name}!")

def calc_kvs_osago(age = 18, experience = 0):
    """Калькулятор выдуманного коэффицента по ОСАГО"""
    min_kvs = 2.27
    final_kvs = min_kvs / age / experience ** 2
    return final_kvs

def calc_kinetic_energy(m: int, v: float):
    """Рассчет кинетической энергии"""
    e = m * v**2 / 2
    return e

def print_credits(*actors):
    """Вывод в консоль титров с именами актеров"""
    print("В главных ролях:\n")
    for actor in actors:
        print(actor + "\n")

def print_check(**goods):
    """Рассчет стоимости покупки товаров и вывод в консоль чека"""
    result = 0
    print("Список покупок:")
    for good, price in goods.items():
        print(good + "\t\t\t" + str(price))
        result += price
    print("Итого:\t" + str(result))

def calc_sales(price):
    """функция, вызывающая внутри себя другую функцию"""
    price *= get_random_num/100
    return price

def example_operation(a, b):
    return a//b

def calculator(a: int, b:int, operation): #1
    """Функция, выполняющая переданную операцию с числами"""
    return operation(a, b)

def example_format(string):
    return "Пользователем введена строка - " + string.upper()

def format_str(string: str, format): #2
    """Функция, выводящая строку определенного переданного формата на экран"""
    print(format(string))

def get_symbol_count(string):
    s_string = set(string)
    symbol_count = dict()
    for s_symbol in s_string:
        symbol_count[s_symbol] = string.count(s_symbol)
    return symbol_count

def print_dict(string, string_function): #3
    """Функция, выводящая словарь символов и их количества в строке"""
    symbol_dict = string_function(string)
    for symbol, count in symbol_dict.items():
        print(f"{symbol} : {count}")

def factorial(number): #1
    if not isinstance(number, int):
        raise TypeError("Число должно быть целым.")
    if number < 0:
        raise ValueError("Число должно быть неотрицательным.")
    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)

def quadratic_equation(a, b, c): #2
    """Решение квадратного уравнения"""
    def discriminant(a, b, c):
        return b**2 - 4 * a * c
    if discriminant(a, b, c) < 0:
        return "Нет корней"
    elif discriminant(a, b, c) == 0:
        return -b / (2 * a)
    else:
        return (-b + discriminant(a, b, c) ** (0.5)) / (2 * a)

print_message = lambda: print("Вывожу какое-то сообщение")
"""лямбда-выражение без параметров"""

third_power = lambda num: num ** 3
"""лямбда-выражение с параметрами"""

def random_example(a, b, c, lambda_example):
    """функция, принимающая лямбда-выражение как параметр, и вызывающая лямбда-выражение внутри себя"""
    a %= b
    b += lambda_example(c) # third_power
    c -= a
    return a + b + c

def count_calls(): #1
    """Отслеживание количества вызовов функции"""
    counter = 0

    def closure(print_result=False):
        nonlocal counter
        if print_result:
            return counter
        counter += 1
        return counter
    return closure

def multiply(num1): #2
    var = 10
    def inner(num2):
        return num1 * num2 + var
    return inner

def a(): #3
    """функция с замыканиями (минимум 3 примера"""
    return 0
