#Создать класс KSLA задать этому классу атрибуты и методы затем создать объекты минимум 10 и вывести их
#на экран


class Car:
    #Создание атрибутов
    def __init__(self, title, color, year, cost, km):
        self.title = title
        self.color = color
        self.year = year
        self.cost = cost

    #создание метода
    def airbag(self):
        return f'в данной машине - {self.title} есть Airbag'

    #тут мы указываем магическим методом функцию для вывода
    def __str__(self):
        return f'Название - {self.title}\n'\
               f'Цвет - {self.color}\n'\
               f'Год выпуска - {self.year}\n'\
               f'Цена - {self.cost}'

#тут мы создаем объект
car1 = Car(title='BMW', color='black', year=1990, cost=3000, km=230.000)
car2 = Car(title='Lexus', color='black', year=2005, cost=15000, km=60.000)
print(car1)
#тут мы вызываем методы
print(car1.airbag())
print('-'*20)
print(car2)
#тут мы вызываем методы
print(car2.airbag())