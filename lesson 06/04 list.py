import random
listNumber =[]
k=6
while k>0:
    x = random.randrange(0, 99, 1)
    listNumber.append(x)
    k=k-1
print(listNumber)

maxNum = max(listNumber)
maxInd = listNumber.index(maxNum)
print("elem: ", maxNum, "index: ", maxInd)

i=0
index=0
max=0
while (i<len(listNumber)):
    if(max < listNumber[i]):
        max=listNumber[i]
        index = i
    i=i+1
print("elem: ", max, "index: ", index)
