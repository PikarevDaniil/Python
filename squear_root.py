from decimal import Decimal
from icecream import ic

def calc_sqrt(acc: Decimal, x: Decimal, y=Decimal(1)):
    if Decimal(y ** 2).quantize(acc) == x.quantize(acc):
        return y.quantize(acc)
    else:
        return calc_sqrt(acc, x, Decimal(y + x/y) / 2)

num = Decimal('37')
acc = Decimal('1.0000')
ic(calc_sqrt(acc, num))
