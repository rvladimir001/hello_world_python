#Создайте функции:
# -генерации двумерного массива случайных чисел с заданными размерами
# -поиска максимальныъ чисел в каждой строке двумерного массива (2 функции)
# -проверки любой переменной на то, что она содержит положительное целое число и приведение переменной к int
#Поместите полученные функции в отдельный модуль.
#Итоговую программу оформите в отдельном модуле (файле).
#Создайте двумерный массив 10х10 из случайных чисел.
#Ввод размера массива сделать с клавиатуры.
#Вычислить максимальный элемент в каждой строке массива
#и вывести полученный список на экран.
from random import randint
import lstcreate
import maxelem

bigArr = lstcreate.TwoDimensionalLisrCreate()
maxElement = maxelem.maxElem(bigArr)
print("Сгенерированный массив: {}".format(bigArr))
print("Значения максимальных элементов из подмассивов: {}".format(maxElement))
