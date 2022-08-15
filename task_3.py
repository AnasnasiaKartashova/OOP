'''
Реализуйте класс MyString, который будет принимать параметр value (любой тип данных) и
сохранять его в виде строки в атрибут класса value.
Для этого типа класса необходимо реализовать возможность сравнения операторами > >= < <= ==.
При проверке необходимо сравнивать не значение атрибута value, а длину значения (строки)
'''

class MyString():
    '''
    Класс MyString принимает любое значение и возвращает строку
    '''

 def __init__(self, value):
     self.value = value

 def __str__ (self):
     return f'{self.value}'


 def __eq__(self, other):
     return self.value == other.value

 def __ne__(self, other):
     return self.value != other.value

 def __lt__(self, other):
     return self.value < other.value

 def __le__(self, other):
     return self.value <= other.value

 def __gt__(self, other):
     return self.value > other.value

 def __ge__(self, other):
     return self.value >= other.value

value_1 = MyString(7)
value_2 = MyString('Привет')

print(value_1.value)
print(value_2.value)
print(value_1 == value_2)
print(value_1 > value_2)
print(value_1 < value_2)


