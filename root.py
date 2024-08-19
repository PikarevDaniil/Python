from decimal import Decimal
from icecream import ic

def calc_sqrt(acc: Decimal, grade: int, x: Decimal, y=Decimal(1)):
    if Decimal(y ** grade).quantize(acc) == x.quantize(acc):
        return y.quantize(acc)
    else:
        print(Decimal((grade - 1) * y + x/(y ** (grade - 1))) / grade)
        return calc_sqrt(acc, grade, x, Decimal((grade - 1) * y + x/(y ** (grade - 1))) / grade)

num = Decimal('4')
grade = 4
acc = Decimal('1.0000')
result = calc_sqrt(acc, grade, num)
ic(result)
