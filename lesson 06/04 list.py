listNumber =[78, 5, 23, 7, 128, 3]
#max с помощью встроенной функции
print(max(listNumber))
#max через цикл
i=0
index=0
max=0
while (i<len(listNumber)):
    if(max < listNumber[i]):
        max=listNumber[i]
        index = i
    i=i+1
print("elem: ", max, "index: ", index)
