#Написать функцию, приминмающую номер месяца и возвращающую время года,
#которому принадледжит месяц. Не забыть про проверки входных данных в самой функции.
#Вызвать функцию в цикле несколько раз для случайных значений номера месяца.
import math
import random
def square(x):
#    if not x.isdigit():
#        print("Введите число!")
#        exit()
    x = int(x)
    if x>0 and x<2 or x==12:
        str="Зима"
    elif x>2 and x<6:
        str="Весна"
    elif x>5 and x<9:
            str="Лето"
    elif x>8 and x<12:
        str="Осень"
    else:
        str="ошибочное значение"
    print("Это {}!".format(str))
    
numberM = input("Введите номер месяца: ")
square(numberM)

for i in range(1, 4):
    r = random.randrange(1, 12, 1)
    print(r)
    square(r)
