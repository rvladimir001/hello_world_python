#Сделать задачу 3 по словарям с текстом из файла song.txt

f = open('song.txt','r')

song =""
for i in f:
    song=song+i
   
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
result = wordSorted(song)
print(result)
