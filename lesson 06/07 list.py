listNumber =[7, 15, 4, 2, 4, 12, 7, 9, 8, 5]
for i in listNumber:
    if(i%3!=0):
        listNumber.remove(i)
print(listNumber)

#i=len(listNumber)
#while i>0:
#    if(i%3!=0):
#        del listNumber[i]
#        i=i-1
#print(listNumber)
