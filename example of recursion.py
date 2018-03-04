# возведене в степень

num = input("число: ",)
n = input("степень: ",)
num = int(num)
n = int(n)
#x - число возводимое в степень, y - степень
def grade(x, y):
    result = 1
    result = result*x
    if result/x != y:
        grade(x, y)
    else:
        return result
        
reply = grade(num, n)
print(reply)
