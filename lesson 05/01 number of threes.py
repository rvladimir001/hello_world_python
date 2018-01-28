num = input("Введите положительное целое трехзначное число: ")

if not num.isdigit():
    print("введите число!")
    exit()
    
x = float(num)
if x>100 or x<999:
    print("число должно быть трехзначным!")
    exit()
    
result = 1
for i in num:
    result=result*int(i)
print("Произведение чисел: ",result)
