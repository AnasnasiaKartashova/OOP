#класс, имитирующий игральный кубик с методом - бросок

import random

class Dice:

    def __init__(self, list_faced):
        self.list_faced = list_faced

value_dice = [Dice(['1', '2', '3', '4', '5', '6'])]

for dice_faced in value_dice:
    value = dice_faced.list_faced
    roll = random.choice(value)
    print("На кубике выпало:", roll)






