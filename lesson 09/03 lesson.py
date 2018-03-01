#from random import randint
#num = int(input("введите размерность списка: ",))
#def listCreate(x):
#    lst = []
#    for i in range(0, x):
#        element = randint(0, 1000)
#        lst.append(element)
#    return lst
#arr = listCreate(num)

#для проверки
#arr = [12, 2, 45, 65, 12, 2, 43, 65]

#numbers = {}
#for k in arr:
#    numbers[k]="0"
#print(len(arr))
#print(len(numbers))
#дан текст:
#Eh bien, mon prince. Gênes et Lucques ne sont plus que des apanages,
#des поместья, de la famille Buonaparte. Non, je vous préviens que si
#vous ne me dites pas que nous avons la guerre, si vous vous permettez
#encore de pallier toutes les infamies, toutes les atrocités de cet
#Antichrist (ma parole, j'y crois) — je ne vous connais plus, vous n'
#êtes plus mon ami, vous n'êtes plus мой верный раб, comme vous dites

#Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
#Слова должны быть отсортированы по убыванию их частоты появления в тексте,
#а при одинаковой частоте появления — в лексикографическом порядке

longStr = "Eh bien, mon prince. Gênes et Lucques ne sont plus que des apanages, des поместья, de la famille Buonaparte. Non, je vous préviens que si vous ne me dites pas que nous avons la guerre, si vous vous permettez encore de pallier toutes les infamies, toutes les atrocités de cet Antichrist (ma parole, j'y crois) — je ne vous connais plus, vous n'êtes plus mon ami, vous n'êtes plus мой верный раб, comme vous dites"
def wordSorted(str1):
    lst = str1.split()
    d = {}
    for i in lst:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    sortD=[]
    for k in d:
        tempLst = (d[k], k)
        sortD.append(tempLst)
    sortD.sort()
    sortD.reverse()
    return sortD
result = wordSorted(longStr)
print(result)
