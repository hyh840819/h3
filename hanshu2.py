# def weight_conver(g):
#     KG = g / 1000
#     return (KG)
#
# g2KG = weight_conver(2500)
# print(str(g2KG) + 'KG')

def g2kg(g):
    return str(g/1000) + 'kg'

print(g2kg(2600))


def sjxbc(a, b):
    return "The right tringle third side's length is {}".format((a**2 + b**2)**(1/2))

print(sjxbc(3, 4))