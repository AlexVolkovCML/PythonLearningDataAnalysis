#-------------------------------------- Задание 1 ---------------------------
# -1.	Имеется строка состоящая из слов. Напишите функцию которая возвращает строку убрав из нее стоп слова.
# Стоп слова находятся в списке: [“Python”, “php”, “go”, “C”]


def new_sring_cut(*args):                                                                  # функция, которая
    new_string = ' '.join(word for word in string.split() if word not in words_to_remove)  # проверяет в данной строке куски текста с разделителем - пробел (.split()) а совпадение с кусками текста из списка стоп-слов. записывает новую строку с разделителем - пробел (''.join)
    return new_string                                                                      # и возвращает новую строчку


string = "Удалить ненужные слова Python php go C"  # проверяемая строка с текстом
words_to_remove = ["Python", "php", "go", "C"]     # стоп-слова, которые надо удалить из текста
print('ответ на задачу 1: ', new_sring_cut(string, words_to_remove))




#-------------------------------------- Задание 2 ---------------------------
# Имеется список, состоящий из чисел.
#Напишите функцию которая принимает число и возвращает список состоящий из элементов первого списка кратных входному параметру.


def func_split(*args):                                                 # функция, которая
    new_list = list(filter(lambda x: x % divider == 0, list_of_nums))   # проверяет в данном списке числа, записывая те, которые делятся на divider без остатка
    return new_list                                                   # и возвращает новый список


list_of_nums = [1, 2, 3, 4, 6, 9]        # проверяемый список
divider = 3                         # делитель
print('ответ на задачу 2: ', func_split(divider))





#-------------------------------------- Задание 3 ---------------------------
# Напишите функцию, которая
# принимает любое количество не именованных аргументов и
# возвращает кортеж состоящий из аргументов у которых тип данных str

def str_cortege(*args):                          # функция, которая
    new_cortege = ()                             # создает новый пустой кортеж

    for item in args:
        if isinstance(item, str):                # проверяет тип данных аргументов во входящем кортеже,
            new_cortege = new_cortege + (item,)  # добавляет в новый кортеж только аргументы, у которых тип данных str
    return new_cortege                           # и возвращает его


print('ответ на задачу 3: ', str_cortege('abc', 'def', 1, 2, 3))


#-------------------------------------- Задание 4 ---------------------------
# Имеются два списка состоящие из произвольных элементов.
# Напишите функцию которая возвращает пересечение списков (элементы которые встречаются и там и там)

def compare_lists(*args):                               # функция, которая
    new_list = list(set(list_1).intersection(list_2))   # сравнивает пересечения в двух данных листах
    return new_list                                     # и возвращает новый лист с совпадающими аргументами


list_1 = [1, 2, 3, 4, 5, 5, 9]
list_2 = [9, 8, 7, 6, 5, 6, 5]
print('ответ на задачу 4: ', compare_lists(list_1, list_2))                    # НЕ ВОЗВРАЩАЕТ ЗНАЧЕНИЯ, КОТОРЫЕ ВСТРЕЧАЮТСЯ ДВАЖДЫ (ТО ЕСТЬ ТЕРЯЕТ ИХ. КАК НЕ ТЕРЯТЬ?)




#-------------------------------------- Задание 5 ---------------------------
# Лесенка.
# Лесенкой - условный набор кубиков, в котором каждый последующий слой содержит меньше кубиков, чем предыдущий.
# Напишите функцию, вычисляющую число лесенок, которое можно построить из n кубиков.
# -	Длина каждой ступени может отличаться.
# -	n - натуральное число в диапазоне от 1 до 100.



def counter(x):                       # функция, вычисляет максимально возможное число столбов из кубиков, образующих лесенку
    height = 1                        # высота первого столба
    count = 0
    for i in range(x):
        if x - height >= 0:           # если оставшихся кубиков, больше, чем высота предыдущего столба +1,
            x = x - height            # вычисляется количество оставшихся кубиков
            count += 1                # к счетчику добавляется единица
            height += 1               # высота последнего столба увеличивается на 1
    return count                      # возвращает максимально возможное число столбов


n = 100
print('ответ на задачу 5: ', counter(n))




#-------------------------------------- Задание 6 ---------------------------
# Напишите декоратор который выводит исключение в случае если декорируемая функция возвращает тип данных отличный от int
# Напишите 2 тестовые декорируемые функции с произвольными данными.


def deco (f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        if all(isinstance(i, int) for i in result) == True:
            return result
        else:
            raise Exception('одна из функций возвращает тип данных отличный от int')
    return wrapper


@deco
def sum_0(c, d):                    # функция 1
    h = (c, d)
    return h


print(sum_0(2, 3))


@deco
def sum_1(c, d):                    # функция 2
    h = (c, d)
    return h


print(sum_1(5, 2))




#-------------------------------------- Задание 7 ---------------------------
# Напишите декоратор который запускает декорируемую функцию повторно, в случае если произошло исключение при первом запуске.
# Напишите 2 тестовые декорируемые функции с произвольными данными.






def deco_2 (f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        try:
            return result
        except result <= 0:
            print('xxx')                        #не печатает :(
        finally:
            return result
    return wrapper

@deco_2
def sum_2(c,d):
    h = c+d
    if h > 0:
        return h
    else:
        raise Exception('h must be >0')      #печатает. ощущение, что все останавливается до декоратора, так как фуекция не возвращает h, а прерывается


print(sum_2(-4, 4))
