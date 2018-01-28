num = input("Введите положительное целое число: ")

if not num.isdigit():
    print("введите цифру!")
    exit()

lenght = len(num)
i = 0
result = 0
while i<lenght:
    if float(num[i])%2 == 0:
        result+=1
    i+=1
print("четных чисел: ",result)
