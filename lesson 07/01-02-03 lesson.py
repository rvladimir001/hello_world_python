#Написать функцию, возвращающую два введеных с клавиатуры числа.
def sum():
    x = input('Первое число: ')
    if not x.isdigit():
        print("введите число!")
        exit()
    y = input('Второе число: ')
    if not y.isdigit():
        print("введите число!")
        exit()
    print("Вы ввели сначала {}, а потом {}".format(x,y))
sum()
