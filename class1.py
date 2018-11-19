class CocaCola:
    formula = ['caffeine', 'sugar', 'water', 'soda']
    # def drink(self):
    #     print("Energy!")
    def drink(self, how_much):
        if how_much == 'a sip':
            print('Cool~')
        elif how_much == 'whole bottle':
            print('Headache!')
        else:
            print("Nothing!")

ice_coke = CocaCola()
ice_coke.drink('a sip')

coke = CocaCola()
coke.drink('xxx')

coke_for_me = CocaCola()
coke_for_you = CocaCola()

print(CocaCola.formula)
print(coke_for_me.formula)
print(coke_for_you.formula)

for element in coke_for_you.formula:
    print(element)

coke_for_China = CocaCola()
coke_for_China.local_logo = '可口可乐'

print(coke_for_China.local_logo)

