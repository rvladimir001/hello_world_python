listNumber =[]
max = 4
i = 0
while i<max:
    num = input("Введите число: ")
    #проверка
    if not num.isdigit():
        print("введите цифру!")
        exit()
        
    listNumber.append(num)
    i+=1
for i in listNumber:
    print(i)
