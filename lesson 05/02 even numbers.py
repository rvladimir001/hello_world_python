num = input("Введите положительное целое число: ")

if not num.isdigit():
    print("введите цифру!")
    exit()

result = 0
for i in num:
    if int(i)%2==0:
        result+=1
print("четных чисел: ",result)
