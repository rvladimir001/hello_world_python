#Использовать функции из задач 1, 2 для решения задания 2 из урока 2:
#Программа, которая считывает два числа и выводит их сумму
num1 = input('Первое число: ')
num2 = input('Второе число: ')
def sum(x, y):
    if not x.isdigit():
        print("введите число!")
        exit()
    if not y.isdigit():
        print("введите число!")
        exit()
    result = int(x)+int(y)
    str = "Сумма двух числе {}".format(result)
    return str
print(sum(num1, num2))
