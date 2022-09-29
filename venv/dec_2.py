#декоратор фильтрующий указаный элемент


def my_filter(any):
    def Oleg_here():
        my_filter = list(filter(lambda x: 'Oleg' not in x, lst))
        print(my_filter)
        return any()

    return Oleg_here

@my_filter
def where_oleg():
    print('А что же с Олегом?')


lst = ['hi','Oleg', 'my', 'Oleg']
where_oleg()





