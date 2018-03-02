#Вводится имя файла. Требуется проверить,
#что его расширение входит в список допустимых (png, jpg, jpeg, gif, svg').

def fileChecked(name):
    lst = name.split(".")
    arr = ['png','jpg', 'jpeg', 'gif', 'svg']
    if lst[1] in arr:
       # f = open(name, "r")
        print("файл открыт для чтения")
    else:
        print("неккоректное расширение файла")

fileName = input("введите название файла: ",)
fileChecked(fileName)
