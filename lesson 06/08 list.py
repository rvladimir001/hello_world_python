import random
listNumber =[]
i=10
while i>0:
    x = random.randrange(0, 99, 1)
    listNumber.append(round(x**0.5))
    i=i-1
print(listNumber)
evenNumbers=[]
unEvenNumbers=[]
for j in listNumber:
    if j%2==0:
        evenNumbers.append(j)
    else:
        unEvenNumbers.append(j)
print( evenNumbers)
print( unEvenNumbers)
