"""Создать классы, спецификации которых приведены ниже.
Определить конструкторы . Определить дополнительно методы __str__.
Определить дополнительно методы в классе, создающие массив объектов.
Задать критерий выбора данных и вывести эти данные на консоль.

Abiturient: id, Фамилия, Имя, Отчество, Адрес, Телефон, Оценки.
Создать массив объектов. Вывести:
    a) список абитуриентов, имеющих неудовлетворительные оценки;
    b) список абитуриентов, у которых сумма баллов выше заданной;
    c) выбрать заданное число n абитуриентов, имеющих самую высокую сумму баллов
(вывести также полный список абитуриентов, имеющих полупроходную сумму)."""
import random

class Abiturient():
    abitur_id = 0
    first_name = ""
    patronymic_name=""
    last_name = ""
    address = ""
    phone = ""
    rating = []
    arr = []

    def __str__(self):
        name = self.last_name+" "+self.first_name+" "+self.patronymic_name
        return "Абитуриент id: {}\nФИО: {}\nАдрес: {}\nТелефон: {}\nОценка: {}".format(self.abitur_id, name.title(), self.address, self.phone, self.rating)
    
    def create_item(self):
        self.abitur_id = random.randrange(1, 1001, 1)
        self.first_name = input("Имя абитуриента: ")
        self.patronymic_name = input("Отчество абитуриента: ")
        self.last_name = input("Фамилия абитуриента: ")
        self.address = input("Адрес абитуриента: ")
        self.phone = input("Телефон абитуриента: ")
        #self.rating = input("Оценка абитуриента: ")
        new_rating = []
        for r in range(0,5):
            new_rating.append(random.randrange(2, 5, 1))
        self.rating = new_rating
        return self

    def create_list(self, num):
        for i in range(0, num):
            self.arr.append(Abiturient().create_item())
        return self.arr
    
new_list_abitur = Abiturient()
new_list_abitur.create_list(2)#всего для трех абитуриентов
#print(new_list_abitur.arr[0])

print("Список абитуриентов с неудовлетворительными оценками")
for ab in new_list_abitur.arr:
    flag = False
    for r in ab.rating:
        if r == 2:
            flag = True
    if flag:
        print(ab.last_name)

print("Список абитуриентов у которых сумма баллов выше 18 быллов")
for ab in new_list_abitur.arr:
    rating_sum = 0
    for r in ab.rating:
        rating_sum=rating_sum+r
    if rating_sum>18:
        print(ab.last_name)

"""
print("Список лучших абитуриентов")
rating_max = 0
for ab in new_list_abitur.arr:
    abitur_d = {}
    rating_sum = 0
    for r in ab.rating:
        rating_sum=rating_sum+r
    if rating_sum>rating_max:
        rating_max = rating_sum


    abitur_d[ab.last_name] = rating_sum
"""
