#Заполнить список из десяти элементов произвольными целочисленными значениями.
#Получить список из элементов певрого списка, стоящих на четных местах.

import random
listNumber =[]
for i in range(1, 11):
    x = random.randrange(0, 100, 1)
    listNumber.append(x)
print(listNumber)

NewListNumber = []
i=0
while (i<len(listNumber)):
    NewListNumber.append(listNumber[i])
    i=i+2
print(NewListNumber)
