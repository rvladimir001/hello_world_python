x = float(input("первае число: "))
y = float(input("второе число: "))
z = float(input("третье число: "))
if (x+y)>z and (x+z)>y and (z+y)>x:
    str="треугольник получится!"
else:
    str="треугольник не получается!"
print(str)
