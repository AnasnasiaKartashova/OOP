class MyString():
    """
    Класс MyString принимает любое значение и возвращает строку
    """

    def __init__(self, value):
        self.value = str(value)

    """
    Методы сравнения >, >=, <, <=,gi == для value
    """
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
print(value_1.value == value_2.value)
print(value_1.value > value_2.value)
print(value_1.value < value_2.value)


