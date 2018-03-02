#Дан список чисел, который может содержать до 100000 чисел
#(каждое число от 0 до 1000).
#Определите, сколько в нем встречается различных чисел.


from random import randint
num = int(input("введите размерность списка: ",))
def listCreate(x):
    lst = []
    for i in range(0, x):
        element = randint(0, 1000)
        lst.append(element)
    return lst
arr = listCreate(num)

#для проверки
#arr = [12, 2, 45, 65, 12, 2, 43, 65]

numbers = {}
for k in arr:
    numbers[k]="0"
print(len(arr))
print(len(numbers))
