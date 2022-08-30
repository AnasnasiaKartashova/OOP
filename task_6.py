"""
Реализуйте класс данных Person, с атрибутами name, surname, age. Для объектов класса должна быть доступна
возможность сравнения операторами >, <, ==. После создания объекта изменение атрибутов должно быть запрещено
"""

class Person():

 """"
 Класс принимает значения имени, фамилии, возраста
 """

 def __init__(self, name, surname, age):
        self.__name = str(name)
        self.__surname = str(surname)
        self.__age = str(age)

 @property
 def name(self):
        return self.__name

 @property
 def surname(self):
        return self.__surname

 @property
 def age(self):
        return self.__age

person_1 = Person('Екатерина', 'Ебонашвили', '20')
print(person_1.name < person_1.surname)
print(person_1.name > person_1.surname)
print(person_1.name == person_1.surname)
print(person_1.age < person_1.surname)