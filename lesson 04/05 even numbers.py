num = float(input("Введите число: "))
i = 0
while num != 0:
    if num % 2 == 0:
        i += 1
    num //= 10
print(i)
