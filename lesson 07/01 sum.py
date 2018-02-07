#Написать функцию, вычисляющую сумму двух переданных чисел.
def sum():
    x = input('Первое число: ')
    if not x.isdigit():
        print("введите число!")
        exit()
    y = input('Второе число: ')
    if not y.isdigit():
        print("введите число!")
        exit()
    print(int(x)+int(y))
sum()
