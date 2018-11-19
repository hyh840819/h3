#!/usr/bin/python
# -*- coding: UTF-8 -*-

class CocaCola:
    formula = ['caffeine', 'sugar', 'water', 'soda']
    def __init__(self, logo_name):
        self.local_logo = logo_name
        # for element in self.formula:
        #     print('Coke has {}!'.format(element))

    def drink(self):
        print('Energy!')

coke = CocaCola('d')
coke.local_logo