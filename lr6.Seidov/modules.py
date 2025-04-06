from file7 import *
import py_compile
import random
import math
import locale
from decimal import Decimal, getcontext
from dataclasses import dataclass
# 1. 7 файлов, в каждом из которых объявлено от 3 разных функций.
# Эти функции МОГУТ реализовывать любой алгоритм.
# В каждом из файлов ДОЛЖНЫ импортироваться функции из других файлов.
# Импорт из файлов в итоге должен представлять собой древовидную структуру, где в файле №1 импортируются функции из файла №2, в файле №2 из файла №3 и т.д.
# Минимальный уровень глубины импортов - 3.

# 2. Функция, в которой демонстрируется работоспособность импортов из п. 1
def print_modules_result(a,b,c,d,e,f):
    print_list_el(a,b,c,f)
    print_list(a,b,c,d,e,f)
    print_sum_lst(a,b,c)

# 3. Файлы байт-кода любых 7 модулей, написанных в течение курса (в том числе модулей этой лабораторной).
py_compile.compile("file1.py")
py_compile.compile("file2.py")
py_compile.compile("file3.py")
py_compile.compile("file4.py")
py_compile.compile("file5.py")
py_compile.compile("file6.py")
py_compile.compile("file7.py")

# 4. Минимум 2 функции, использующие разные методы из модуля random
def random_number(start, end):
    return random.randint(start, end)

def random_choice_from_list(lst):
    return random.choice(lst)

# 5. Минимум 3 функций, использующих разные методы из модуля math
def square_root(x):
    return math.sqrt(x)

def factorial(n):
    return math.factorial(n)

def round_up(x):
    return math.ceil(x)

# 6. Минимум 3 функции, использующие разные методы из модуля locale
def set_and_get_locale():
    locale.setlocale(locale.LC_ALL, '')
    return locale.getlocale()

def format_number_with_locale(number):
    locale.setlocale(locale.LC_ALL, '')
    return locale.format_string("%d", number, grouping=True)

def format_currency(value):
    locale.setlocale(locale.LC_ALL, '')
    return locale.currency(value, grouping=True)

# 7. Минимум 2 функции, использующие разные методы из модуля decimal
def precise_division(a, b):
    return Decimal(a) / Decimal(b)

def set_precision_and_round(value, precision):
    getcontext().prec = precision
    return Decimal(value)

# 8. Минимум 3 разных data-класса.
@dataclass
class Book:
    title: str
    author: str

@dataclass
class Student:
    name: str
    surname: str
    age: int
    grades: list

@dataclass
class Car:
    make: str
    model: str
    year: int
    mileage: float

# 9. Минимум 5 функций, использующих в своей работе описанные в п. 7 data-классы
# В функции ДОЛЖНО быть, как минимум, следующее:
# 9.1. Передача объекта data-класса как параметр
def print_book_details(book: Book):
    print(f"Название книги: {book.title}, автор: {book.author}")

# 9.2. Работа со списком из объектов data-классов
def average_student_age(students: list[Student]):
    return sum(student.age for student in students) / len(students)

# 9.3. Работа со словарём, где в качестве значения выступает объект data-класса
def get_car_by_model(cars: dict[str, Car], model: str):
    return cars.get(model)

# 9.4. Модификация значений объекта data-класса
def update_car_mileage(car: Car, new_mileage: float):
    car.mileage = new_mileage

# 9.5. Создание объекта data-класса на основе передаваемых параметров
def create_new_student(name: str, surname:str, age: int, grades: list):
    return Student(name, surname, age, grades)

