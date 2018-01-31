import random
listNumber =[]
i=6
while i>0:
    x = random.randrange(0, 99, 1)
    listNumber.append(x)
    i=i-1
print(listNumber)#список как есть
for i in listNumber:#вывод чере цикл
    print(i)
