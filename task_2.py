class Student():
    '''
    Класс Student включает в себя информацию о студентах: имя, фамилия, номер группы и список оценок
    '''

    def __init__(self, first_name: str, last_name: str, group: str):
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.marks = []

    def add_mark(self):
        '''
        Функция добавляет оценку в список оценок студента, если она больше 0 и меньше 11
        '''

        if self.marks == int and 0 < self.marks < 11:
            self.marks.append(marks)
            print('Оценка добавлена')
        else:
            print('Введите верный формат оценки от 1 до 10')

    def get_average_mark(self):
        '''
        Функция считает средний балл студента
        '''

        if len(self.marks) == 0:
            return 0
        else:
            return sum(self.marks) / len(self.marks)

    def get_scolarship(self):
        '''
        Функция возращает размер стипендии студента
        '''

        if self.get_average_mark() >= 5:
            return 'Этот студент получает стипендию в размере 500 рублей'
        else:
            return 'Этот студент получает стипендию в размере 150 рублей'


class Aspirant(Student):
    '''
    Класс Aspirant - наследник Student, включает в себя информацию о студентах:
    имя, фамилия, номер группы, список оценок, публикации
    '''

    def __init__(self, first_name: str, last_name: str, group: str, scientific_publications: str):
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.marks = []
        self.scientific_publications = scientific_publications

    def get_scolarship(self):
        '''
        Функция возращает размер стипендии аспиранта
        '''

        if self.get_average_mark() >= 5:
            return 'Этот аспирант получает стипендию в размере 700 рублей'
        else:
            return 'Этот аспирант получает стипендию в размере 250 рублей'

p = Student('Иван', 'Пупкин', 'П-41')
p.marks = 5, 1, 6

print('Имя: ', p.first_name)
print('Фамилия: ', p.last_name)
print('Группа: ', p.group)
print('Оценки: ', p.marks)
print (p.get_average_mark())
print (p.get_scolarship())
print()

a = Aspirant ('Мария', 'Шишкина', 'П-51', 'Теория атома')
a.marks = 9, 10, 8
print('Имя: ', a.first_name)
print('Фамилия: ', a.last_name)
print('Группа: ', a.group)
print('Оценки: ', a.marks)
print('Публикации: ', a.scientific_publications)
print (a.get_average_mark())
print (a.get_scolarship())
