#класс, имитирующий игральный кубик с методом - бросок

from random import choice


class Dice:

    def __init__(self, list_faced):
        list_faced = list(range(1, list_faced + 1))
        self.list_faced = list_faced

    def roll_dice(self):
        roll = choice(self.list_faced)
        print("На кубике выпало:", roll)
        return roll


dice_1 = Dice(20)
dice_1.roll_dice()



