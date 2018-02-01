import random
listNumber =[]
k=6
while k>0:
    x = random.randrange(0, 99, 1)
    listNumber.append(x)
    k=k-1
print(listNumber)

NewListNumber = []
i = len(listNumber)-1
while i>-1:
    elem = listNumber[i]
    NewListNumber.append(elem)
    i = i-1
print(NewListNumber)

listNumber.reverse()
print(listNumber)
