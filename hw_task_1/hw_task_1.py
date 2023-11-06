#------------------- задание1 ---------------------------
#----Напишите функцию которая возвращает длину принимаемой строки, по умолчанию строка пустая (s=’’). Пропишите все аннотации


s = ''                                 #переменная, по умолчанию имеет длину 0
def return_len_str(lengh):             # функция, которая возвращает длину принимаемой строки s
    leng_str_s = (len(lengh))          # операция, которая считает длину принимаемой строки s
    print('Ответ к заданию 1: Длина принимаемой строки составляет ',leng_str_s)    # операция, которая выводит на печать длину принимаемой строки s


return_len_str(s)


#------------------- задание2.1 ---------------------------
#-----Напишите функцию которая
# a)	принимает два списка
# b)	возвращает длину самого длинного

list_1 = [1,2,3]
list_2 = [1,2,3]

def retern_longer_list(num1,num2):
    if len(num1)>len(num2):
        longer_len = len(num1)
        print('Ответ к заданию 2.1, длина большего списка составляет:',longer_len)
    elif len(num2)>len(num1):
        longer_len = len(num2)
        print('Ответ к заданию 2.1, длина большего списка составляет:',longer_len)
    else:
        longer_len = len(num1)
        print('Ответ к заданию 2.1: Длина списков одинакова и сотавляет ', longer_len, 'символа(-ов)')


retern_longer_list(list_1,list_2)


#------------------- задание2.2 ---------------------------
# (более короткий вариант)

list_1 = [1,2,36,2]
list_2 = [1,2,3]

def retern_longer_list(num1,num2):
    if len(num1)>len(num2):
        longer_len = len(num1)
        print('Ответ к заданию 2.2:',len(num1))
    else:
        print('Ответ к заданию 2.2:', len(num2))


retern_longer_list(list_1,list_2)


#------------------- задание3 ---------------------------
#-----Напишите функцию которая:
# a)	принимает список с произвольными значениями
# b)	добавляет к нему произвольное значение
# c)	возвращает результирующий список

list_1 = [1,'два',3]         #список с произвольными значениями
random_value = 'четыре'      #произвольное значение

def retern_list_add_ren_val (num1,num2):
    new_list = num1                      #переменной присваивается список list_1
    new_list.append(num2)                #к списку добавляется произвольное значение random_value
    print('Ответ к заданию 3:',new_list) #вывод нового списка


retern_list_add_ren_val(list_1,random_value)




#------------------- задание4 ---------------------------
#       Напишите функцию которая
# a)	принимает число
# b)	Если число больше 100 или меньше -100, то вывести в консоль символ “-”, иначе вывести на экран символ “+”

random_value = 155                          #ввод случайного значения

def compare_range (num1):
    if num1 < -100 or num1 > 100:           #сравнение значения с требуемым диапазоном
        print('Ответ к заданию 4: -')       #вывод, если значение переменной вне диапазона
    else:
        print('Ответ к заданию 4: +')       #вывод, если значение переменной поадает в диапазон


compare_range (random_value)





#------------------- задание5 ---------------------------
#       Напишите функцию которая отвечает “ДА” или “НЕТ” на вопрос:
#       содержит ли текст строки 1 в себе текст из строки 2?

str_1 = '12tes56565635test12'     # список 1
str_2 = 'test'                    # список 2


def match_strings(string_1, string_2):
    counter_1 = 0  # счетчик списка 1
    counter_2 = 0  # счетчик списка 2
    count_compare = 0  # счетчик совпадений символов из двух сравниваемых списков

    a = str_1[counter_1]  # значение символа в списке 1 с порядковым номером из счетчика 1
    b = str_2[counter_2]  # значение символа в списке 2 с порядковым номером из счетчика 2

    N1 = len(str_1)  # длина списка 1
    N2 = len(str_2)  # длина списка 2
    for i in range(N1):            # сравнение символов двух списков в цикле от единицы до значения длины списка 1


        if a == b:                      #если значения символов совпали
            count_compare += 1            # то счетчик сопадений увеличивается на 1
            if count_compare < N2:             # если при этом счетчик значений меньше длины списка 2 (значит совпадение всей длины списка 2 еще не найдено)
                counter_1 +=1                    # поэтому счетчики списков также увеличиваются на 1
                counter_2 +=1
                a = string_1[counter_1]             # что отражается на значениях a,b
                b = string_2[counter_2]
            else:
                print('Ответ на задание 5: ДА')     # если счетчик значений равен длине списка 2, значит полное совпадение списка 2 в списке 1 найдено
                break                            # совпадение найдено, цикл обрывается.

        else:                           #если значения символов не совпали
            counter_1 += 1                # то счетчик списка 1 увеличивается на единицу (чтоб сравнивать следующий символ)
            counter_2 = 0                 # а счетчик списка 2 сбрасывается, чтобы далее сравнивать следующее значение из списка 2 с первым символом из списка 1
            a = string_1[counter_1]          # что отражается на значениях a,b
            b = string_2[counter_2]
            count_compare=0               # счетчик совпадений также сбрасывается
            if counter_1 == N1-1:
                print('Ответ на задание 5: НЕТ')


match_strings(str_1,str_2)

#------------------- задание5.2 --------------------------
# Проще: перебирать не символы, а диапазоны списка a[0:4] и b[i:i+4], где в цикле от 0 до длины списка b

