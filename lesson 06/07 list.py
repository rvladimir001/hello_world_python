import random
listNumber =[]
k=10
while k>0:
    x = random.randrange(0, 99, 1)
    listNumber.append(x)
    k=k-1
print(listNumber)

for i in listNumber:
    if(i%3!=0):
        listNumber.remove(i)
print(listNumber)
