# Простая программа мини-викторина

import random
class Mystery:

    def __init__(self, question, answer, list_of_wrong_choices):
        self.question = question
        self.answer = answer
        self.list_of_wrong_choices = list_of_wrong_choices

lst_of_wrong_choices = [Mystery('Как джуну из РБ попасть в айти в 2022?',
                                'Уехать из РБ',
                                ['Молиться', 'Принести голубя в жертву', 'Даже не пытаться']),
                        Mystery('А как выучить питон?',
                                'Зубрить днями и ночами',
                                ['Прочитать одну книгу', 'Смотреть видео "выучь питон за час"', 'с божьей помощью'])]

random.shuffle(lst_of_wrong_choices)

for mystery_item in lst_of_wrong_choices:
    print(mystery_item.question)
    print('Варианты ответов: ')
    any_answer = mystery_item.list_of_wrong_choices + [mystery_item.answer]
    random.shuffle(any_answer)
    count = 0

    while count < len(any_answer):
        print(str(count+1) + ". " + any_answer[count])
        count += 1
    print('Введите номер вашего ответа: ')
    user_answer = input()

    while not user_answer.isdigit():
        print('Введите корректное число: ')
        user_answer = input()
    user_answer = int(user_answer)

    while not (user_answer > 0 and user_answer <= len(any_answer)):
        print('Неккоректное число, введите число вашего ответа: ')
        user_answer = input()

    if any_answer[user_answer-1] == mystery_item.answer:
        print('Верно')

    else:
        print('Неверно')



