#Программа должна подсчитать количество строк, слов и букв в переданном ей файле.
#Имя файла должно передаваться в качестве первого аргумента после имени самого
#скрипта. Например, вызов скрипта в Linux через командную оболочку выглядит
#примерно так: python3 words.py text.txt
f = open('text.txt','r')
countStr = 0
str1 = ""
for line in f:
    countStr=countStr+1
    str1 = str1+line
lstline = len(str1.split())
#letters = len(str1)

letters = 0
for k in str1:
    if k==" ":
        continue
    elif k=="\n":
        continue
    else:
        letters=letters+1
        
f.close()

print("Строк: {} Слов: {} Букв: {}".format(countStr, lstline, letters))
