#Заполнить список из шести элементов произвольными целочисленными значениями.
#Вывести список на экран в обратной последовательности. Два варианта получения
#обратной последовательности: с приминением цикла и без него.

import random
listNumber =[]
k=6
while k>0:
    x = random.randrange(0, 99, 1)
    listNumber.append(x)
    k=k-1
print(listNumber)

NewListNumber = []
i = len(listNumber)-1
while i>-1:
    elem = listNumber[i]
    NewListNumber.append(elem)
    i = i-1
print(NewListNumber)

listNumber.reverse()
print(listNumber)

# 2 вариант с for
import random
listNumber =[]
NewListNumber=[]
for i in range(1, 7):
    x = random.randrange(0, 100, 1)
    listNumber.append(x)
print(listNumber)
listNumber.reverse()
print(listNumber)

