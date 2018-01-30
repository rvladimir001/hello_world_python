import random
listNumber =[]
i=10
while i>0:
    x = random.randrange(0, 99, 1)
    listNumber.append(round(x**0.5))
    i=i-1
print(listNumber)
