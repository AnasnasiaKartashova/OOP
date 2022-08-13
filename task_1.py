# создаем класс Nobody
class Nobody():

    # создаем классу Nobody атрибут name
    def __init__(self, name):  
        self.name = name

        # Задаем условия для класса
        if name == 'Nobody':
            self.name = 'Nobody'
        
        #Если значение не Nobody, то сохранить как I'm Nobody, not <name>
        else:
            self.name = 'Im Nobody, not ' + str(name)

Nastya = Nobody('Nastya')
Nobody = Nobody('Nobody')

print(Nastya.name)
print(Nobody.name)
