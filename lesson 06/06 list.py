#Заполнить список из шести элементов квадратными корнями
#произвольныз целочисленныз значений.
#Вывести список на экран через запятую.

import random
import math
listNumber =[]
WListNumber =[]
i=10
while i>0:
    x = random.randrange(0, 99, 1)
    listNumber.append(round(x**0.5))
    i=i-1
print(listNumber)

#второй вариант с библиотекой math
for j in range(1, 11):
    y = random.randrange(0, 99, 1)
    WListNumber.append(round(math.sqrt(y)))
print(WListNumber)
