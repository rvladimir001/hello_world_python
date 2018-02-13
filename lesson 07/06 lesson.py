#Работаем с чужим кодом. В коде из файла
#https://github.com/groall/python_learning/blob/master/lesson_04_cycles/task03.py
#нужно заменить повторяющееся в циклах действие суммирования на вызов функции,
#функция должна работать с глобальной переменной sumNumbers.

# Пользователь вводит любое целое положительное число (сделать проверку).
# Программа должна просуммировать все числа от 1 до введенного пользователем числа (не включая его).

x = input('Введите целое положительное число: ')

if not x.isdigit():
    print("Вы ввели не число")
    exit()

xInt = int(x)
if xInt < 1:
    print("Число не положительное")
    exit()

def sumN(numb):
    global sumNumbers
    for i in range(1, numb+1):
        sumNumbers += i

sumNumbers = 0
sumN(xInt)
print("Сумма", sumNumbers)


