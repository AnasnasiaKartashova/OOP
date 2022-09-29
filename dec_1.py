'''декоратор разворачивающий аргументы
'''

def reverse(func_1_value):
    def func_1(value):
        value_rev = list(reversed(value))
        print(value_rev)
        func_1_value()

    return func_1

@reverse
def func():
    return

func('Привет')
func('Как дела?')



