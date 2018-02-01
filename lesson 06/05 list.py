import random
listNumber =[]
k=10
while k>0:
    x = random.randrange(0, 99, 1)
    listNumber.append(x)
    k=k-1
print(listNumber)

NewListNumber = []
i=2
while (i<len(listNumber)):
    NewListNumber.append(listNumber[i])
    i=i+2
print(NewListNumber)
