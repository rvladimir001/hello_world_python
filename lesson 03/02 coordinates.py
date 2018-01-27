num1 = float(input("введите первую цифру:"))
num2 = float(input("введите вторую цифру:"))
if num1>0 and num2>0:
    print("Первая четверть!!!")
elif num1>0 and num2<0:
    print("Вторая четверть!!!")
elif num1>0 and num2>0:
    print("Третья четверть!!!")
elif num1<0 and num2>0:
    print("Четвертая четверть!!!")
else:
    print("Начало координат!")
