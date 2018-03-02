#f = open('myFile.py', 'a')
#f.write('hello')
#f.close()

#f = open('myFile.py', 'r')
#f.read()

f = open('text.txt','r')
for line in f:
    print(line)
f.close()

l = [12, 23, 5, 52, 97]

f = open('text.txt','w')
for index in l:
    f.write(str(index)+ '\n')
f.close()

f = open('text.txt','r')
for line in f:
    print(line)
f.close()
