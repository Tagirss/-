def operations():
    """Операции"""
    #Арифметические операции, присваивание и работа с переменными
    print(4 + 3)
    A = 5 - 8
    B = A / (-1)
    C = 4 % 3 // 2
    A *= C
    D = B**3 + C
    print(A, B, C, D)
    print(round(4.5))
    # Преобразование
    F = int(4.8)
    AGE = str(5)
    print("Пете " + AGE + " лет")
    # Логические
    print(not(True or False and False))
    SUN = "sun"
    SUNSHINE = "sunshine"
    print(SUN in SUNSHINE)
    DD = 2
    print(DD != '2')
    #Условные
    if (A == 3):
        print("A = 3")
    else:
        print("A != 3")
    #Циклы
    print("Цикл 1")
    for n in range(0, 10, 2):
        print(n)
    L=10
    print("Цикл 2")
    while L > 0:
        print(L)
        L-=2
    # Цикл do-while можно только эмулировать
    #Функции
    def print_smth(string: str):
        """ Функция для вывода сообщения в консоль """
        print(string + " - эта строка выведена с помощью функции printSMTH")
    print_smth("aabbcc")
