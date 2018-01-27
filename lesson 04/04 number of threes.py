num = float(input("Введите число: "))
num1 = num%100%10#последнее число
num2 = num%100//10#среднее число
num3 = num//100#первое число
print(num1*num2*num3)
