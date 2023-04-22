#\*************************/#
#\*******Te3K@_PaynE*******/#
#\**79811131773@yandex.ru**/#
#\*************************/#

'''
В фермерском хозяйстве в Карелии выращивают чернику.
Она растёт на круглой грядке, причём кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних.
Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью,
поэтому ко времени сбора на них выросло различное число ягод
— на i-ом кусте выросло ai ягод.
(В нашем случае - случайное число от 0 до 100)
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод,
которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки.
'''

import random

# Функция вывода автора программы
def author():
    print('****************************')
    print('Программа создана:')
    print('Илья "Te3K@_PaynE" Новичихин')
    print('79811131773@yandex.ru')
    print('****************************')

_n = int(input("Введите количество кустов черники: "))
_list_chernika = list()
for i in range(_n):
    _list_chernika.append(random.randint(0, 100))
print(_list_chernika)
_list_res_chernika = list()
for i in range(_n):
    res = _list_chernika[i - 2] + _list_chernika[i - 1] + _list_chernika[i]
    _list_res_chernika.append(res)
print(_list_res_chernika)
print(f'Максимальное количество ягод, которое можно собрать = {max(_list_res_chernika)}')