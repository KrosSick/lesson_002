#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.insert(1, 'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
birds.discard
#  и выведите список на консоль
# TODO здесь ваш код
zoo.append(birds)
print(zoo)

zoo = zoo + birds
print(zoo)
# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.

print(zoo.index('kangaroo'))

