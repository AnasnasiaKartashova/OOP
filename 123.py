'''Реализуйте итератор Counter, который принимает параметр start, а также step и stop
(два последних – опционально). На каждой итерации значение должно изменяться на 1 или на значение step
(если оно задано). Если значение превысит значение stop – вызвать исключение StopIteration
'''

class Counter():

    def __init__(self, start, step = 1, stop = None):
        self.start = int(start)
        self.step = step
        self.stop = stop

    def __next__(self):







