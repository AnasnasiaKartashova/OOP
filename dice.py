#класс, имитирующий игральный кубик с методом - бросок

from random import choice

class Dice:

   def __init__(self, *list_faced):
        self.list_faced = list(list_faced)

   def roll_dice(self):
        roll = choice(self.list_faced)
        print("На кубике выпало:", roll)
        return roll

dice_1 = Dice('1', '2', '3', '4', '5', '6','7','8','9',
               '10','11','12','13','14','15','16','17',
               '18','19','20')

dice_1.roll_dice()






