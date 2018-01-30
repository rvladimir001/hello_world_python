listNumber =[78, 5, 23, 7, 128, 3]
NewListNumber = []
#обратная последовательность с помощью цикла
i = len(listNumber)-1
while i>-1:
    elem = listNumber[i]
    NewListNumber.append(elem)
    i = i-1
print(NewListNumber)
#обратная последовательность c помощью метода reverse
listNumber.reverse()
print(listNumber)
