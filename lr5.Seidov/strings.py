import random
# 1. Функция, принимающая на вход список.
# Функция возвращает перевёрнутый список.
def reverse_list(lst):
    return lst[::-1]

# 2. Функция, принимающая на вход список.
# Функция изменяет одно, несколько или все значения списка.
# Функция возвращает изменённый список. 
def modify_list(lst, index, value):
    lst[index] = value
    return lst

# 3. Функция, принимающая на вход два или более списков.
# Функция сравнивает переданные на вход списки.
# Функция возвращает отметку, равны или нет все переданные на вход списки.
def compare_lists(*args):
    if all(lst == args[0] for lst in args):
        return True
    return False

# 4. Функция, принимающая на вход список и доп. параметры (необходимо самостоятельно их определить). 
# Функция ДОЛЖНА иметь возможность выбрать диапазон значений из переданного списка с заданным шагом.
# Нужно рассмотреть все возможные ситуации, связанные с передаваемыми значениями.
# Функция возвращает список, соответствующий диапазону.
def select_range(lst, start, end, step=1):
    return lst[start:end:step]

# 5. Функция, принимающая на вход некие параметры.
# Функция создаёт список, основываясь на переданных параметрах.
# Создание списка, его наполнение и возврат полученного списка.
def create_list(*args):
    return list(args)

# 6. Функция, принимающая принимающая на вход список и доп. параметры (необходимо самостоятельно их определить).
# Функция вставляет элемент в заданную позицию списка.
# Функция возвращает изменённый список.
def insert_element(lst, index, value):
    lst.insert(index, value)
    return lst

# 7. Функция, принимающая на вход два или более списков и доп. параметры (необходимо самостоятельно их определить)..
# Функция объединяет все переданные на вход списки и сортирует их желаемым образом.
# Функция возвращает результирующий список. 
def merge_and_sort_lists(parametr, *args):
    merged = []
    for lst in args:
        merged.extend(lst)
    return sorted(merged, key=parametr)

# 8. Функция, не принимающая никаких параметров.
# Функция создаёт список из целых чисел произвольной длины.
# Функция проверяет, длина списка чётное число или нет.
# Если чётное, то функция сообщает об этом и создаёт новые списки до тех пор, пока не будет создан список нечётной длины.
# Если нечётное, то функция ищет центральный элемент списка и выводит количество элементов с таким же значением, что и у центрального элемента.
def create_and_check_list():
    lst = random.sample(range(1, 101), random.randint(1, 20))
    while len(lst) % 2 == 0:
        print("Длина списка чётная.")
        lst = random.sample(range(1, 101), random.randint(1, 20))
    central_element = lst[len(lst) // 2]
    count = lst.count(central_element)
    print(f"Центральный элемент: {central_element}, его количество: {count}")

# 9. Функция, прибавляющая к первому списку другие списки.
# Если длина первого списка превышает заданный порог, необходимо удалить из списка некоторые элементы, чтобы число элементов списка не превышало порог.
# Функция возвращает изменённый первый список.
def merge_with_limit(lst, *args, limit):
    lst.extend([item for sublist in args for item in sublist])
    if len(lst) > limit:
        lst = lst[:limit]
    return lst

# 10. Минимум 6 функций, которые сортируют список по заданным критериям.
# Минимум 3 из этих функций ДОЛЖНЫ использовать функцию map()
def sort_ascending(lst):
    return sorted(lst)

def sort_descending(lst):
    return sorted(lst, reverse=True)

def sort_by_length(lst):
    return sorted(lst, key=len)

def sort_by_square(numbers):
    squared_numbers = list(map(lambda x: x**2, numbers))
    return sorted(squared_numbers)

def sort_uppercase(strings):
    upper_strings = list(map(str.upper, strings))
    return sorted(upper_strings)

def sort_by_vowel_count(strings):
    def count_vowels(s):
        return sum(map(s.lower().count, "аоуяюеёиэ"))
    return sorted(strings, key=count_vowels)

# 11. Функция, которая извлекает с удалением минимальный элемент списка.
# Функция возвращает минимальный элемент списка.
def extract_min(lst):
    min_val = min(lst)
    lst.remove(min_val)
    return min_val

# 12. Минимум 2 функции, принимающие на вход один или несколько кортежей, и, ВОЗМОЖНО, доп. параметры.
# Функции совершают некие операции над кортежем или кортежами.
# Функции МОГУТ возвращать некоторые значения.
def sum_tuples(*args):
    return sum(args, ())

def count_occurrences(tpl, value):
    return tpl.count(value)

# 13. Функция, принимающая на вход кортеж неопределённой длины, содержащий произвольные значения.
# Функция перебирает элементы кортежа и формирует новый кортеж, состоящий из типов данных каждого элемента входного кортежа.
# Функция возвращает кортеж из типов данных.
def tuple_types(*args):
    return tuple(type(arg) for arg in args)

# 14. Функция, принимающая на вход кортеж и доп. параметры (необходимо самостоятельно их определить).
# Функция проверяет, есть ли заданный элемент в кортеже.
# Функция возвращает отметку, есть элемент или нет.
def check_in_tuple(tpl, element):
    return element in tpl

# 15. Функция, принимающая на вход один или несколько списков, и, возможно, доп. параметры.
# Функция формирует двумерный список по произвольным критериям и возвращает этот список.
def create_2d_list(*lists, fill_value=0, max_length=None):
    if max_length is None:
        max_length = max(len(lst) for lst in lists)
    two_d_list = [lst[:max_length] + [fill_value] * (max_length - len(lst)) for lst in lists]
    return two_d_list

# 16. Минимум 3 функции, которые принимают на вход словарь.
# Функции совершают некие операции над словарём.
# Функции возвращают какое-либо значениЕ, значениЯ.
def get_keys(d):
    return d.keys()

def get_values(d):
    return d.values()

def get_item(d, key):
    return d.get(key, None)

# 17. Функция, принимающая на вход два или более словарей и доп. параметры (необходимо самостоятельно их определить).
# Функция считает, сколько раз встречается элемент с определённым ключом во всех словарях суммарно и выводит это значение (например, если есть 3 словаря, в двух из них есть элемент с ключом 'name', а в третьем нет, то выводится значение 2).
def count_key_occurrences(*dicts, key):
    if not dicts:
        return 0
    count = 0
    for dict in dicts:
        for dict_key in dict.keys():
            if dict_key == key: count +=1 
    return count

# 18. Функция, принимающая на вход комплексный словарь определённого формата, у которого будет минимум 3 уровня вложенности.
# Функция ищет в этом словаре определённый элемент или элементы, располагающиеся на самом последнем уровне вложенности.
# Функция возвращает значение найденного элемента или элементов или None, если такой элемент или элементы не найдены.
def find_element(d, target):
    if isinstance(d, dict):
        for key, value in d.items():
            if key == target:
                return value
            elif isinstance(value, dict):
                result = find_element(value, target)
                if result:
                    return result
    return None

# 19. Функция, вызывающая все другие функции из шагов 1-18