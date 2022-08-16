class Kg():
'''
Класс принимает значения float и возвращает  в виде результата значение в килограммах
по значениям: тонна, центнер, фунт, пуд
'''
    def __init__(self, kg):
        self.kg = float(kg)
    '''
    Методы перевода килограмм в тонны, центнеры, фунты и пуды
    '''
    def ton(self):
        return self.kg * 1000

    def centner(self):
        return self.kg * 100

    def pound(self):
        return self.kg * 2.2046

    def pud(self):
        return self.kg * 0.0610475

value_1 = Kg(1)
value_2 = Kg(3.5768)

print('Значение тонны в кг:', value_1.ton())
print('Значение тонны в кг:', value_2.ton())
print()
print('Значение центнера в кг:', value_1.centner())
print('Значение центнера в кг:', value_2.centner())
print()
print('Значение фунта в кг:', value_1.pound())
print('Значение фунта в кг:', value_2.pound())
print()
print('Значение пуда в кг:', value_1.pud())
print('Значение пуда в кг:', value_2.pud())


