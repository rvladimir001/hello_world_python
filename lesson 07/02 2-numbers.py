#Написать функцию, возвращающую два введеных с клавиатуры числа.
num1 = input('Первое число: ')
num2 = input('Второе число: ')
def sum(x,y):
    if not x.isdigit():
        print("введите число!")
        exit()
    if not y.isdigit():
        print("введите число!")
        exit()
    str ="Вы ввели сначала {}, а потом {}".format(x,y)
    return str
print(sum(num1, num2))
