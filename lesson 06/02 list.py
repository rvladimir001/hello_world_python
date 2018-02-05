#Заполнить список из четырёх элементов введёными строковыми значениями. Вывести список на экран.

listNumber =[]
for i in range(1, 5):
    num = input("Введите число: ")
    listNumber.append(num)
print(listNumber)
