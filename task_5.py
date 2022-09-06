'''
Реализуйте класс Person, который имеет атрибуты name, surname, age.
Атрибуты name и surname должно быть запрещено изменять, обращаясь по имени.
Атрибут age можно изменять только на +1 год (в противном случае - выдавать сообщение об ошибке).
Реализовать свойство full_name, которое будет возвращать строку из значений имени и фамилии через пробел
'''


class Person():

 """"
 Класс принимает значения имени, фамилии, возраста
 """

 def __init__(self, name, surname, age):
        self.__name = str(name)
        self.__surname = str(surname)
        self.__age = int(age)

 """
 Функции для запрета изменения атрибутов
 """
 @property
 def name(self):
        return self.__name

 @property
 def surname(self):
        return self.__surname

 @property
 def age(self):
        return self.__age

 """
 Возраст можно изменить только на +1
 """
 @age.setter
 def age(self, value):
        if (value - self.age > 1):
            print('Нельзя увеличить/уменьшить возраст больше, чем на 1 год')
            return

        self.__age = value

 """
 Функция, которая выводит строку с именем и фамилией
  """
 def full_name_person(self):
        return f'Полное имя: {self.name} {self.surname}'


person_1 = Person('Екатерина', 'Ебонашвили', 20)
print(person_1.name)
print(person_1.surname)
print(person_1.age)
print()

person_1.age += 2
print(person_1.age)
person_1.age += 1
print(person_1.age)
print(person_1.full_name_person())


