num = input("Введите положительное целое трехзначное число: ")

if not num.isdigit():
    print("введите число!")
    exit()
    
x = float(num)
if x>100 or x<999:
    print("число должно быть трехзначным!")
    exit()
    
lenght = len(num)
i = 0
result = 1;
while i<lenght:
    result*=float(num[i])
    i+=1
print("произведение трех введенных числе: ",result)
