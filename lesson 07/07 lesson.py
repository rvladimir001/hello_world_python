#Написать функцию расчета аннуитетного платежа.
#Написать функцию расчета ежимесячного платежа.
#Рассчитать размер платежа при ипотеке 15 млн на 25 лет под 14% годовых.
#Мат. часть:
#http://biznes-kredit.info/malyj/raschet-annuitetnyh-platezhej-formula-excel.html

totalSum = 15000000     #сумма кредита
time = 25*12            #срок кредита в меяцах
percent = 14/12/100     #месячный процент

def payment(totalS, t, perc):
    k = (perc*((1+perc)**t))/(((1+perc)**t)-1)
    pay = k*totalS
    return round(pay, 2)
    
print("Ежемесячный платеж {} рублей".format(payment(totalSum, time, percent)))
