#Сделать задачу 3 по словарям с текстом из файла song.txt

file = open('codes.txt','r')
cipher = "006005034028017006029034028017006006017036034028020021029034028017028017"

song =""
   
def createDic(f):
    dic = {}
    for line in f:
        tempLst = line.split()
        value = tempLst[0]
        key = tempLst[1]
        dic[key]=value
    return dic

def strToLst(s):
    cipherLst=[]
    j = 0
    k = 3
    i = 0
    lenght = len(cipher)/3
    while i<lenght:
        elem = s[j:k]
        cipherLst.append(elem)
        j=j+3
        k=k+3
        i=i+1
    return cipherLst

lstCodes = createDic(file)
lstCipher = strToLst(cipher)

sentence = ""
for r in lstCipher:
    sentence = sentence + lstCodes[r]
print(sentence)
