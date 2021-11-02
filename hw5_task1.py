"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре
квартала для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple
from functools import reduce

Company = namedtuple('Company', ['name', 'q1', 'q2', 'q3', 'q4'])
num = int(input("Введите количество компаний "))
companies = []
for i in range(num):
    companies.append(Company._make(
        input("Введите через пробел название компании и значения ее прибыли за четыре квартала ").split(' ')))

cum_profit = list(map(lambda c: int(c.q1) + int(c.q2) + int(c.q3) + int(c.q4), companies))
av_profit = sum(cum_profit) / len(cum_profit)
print(f"Средняя прибыль рассматриваемых компаний за год = {av_profit :.2f}")

for c in companies:
    if reduce(lambda a, b: a + b, [int(getattr(c, field)) for field in c._fields[1:]]) <= av_profit:
        print(f"Прибыль компании {c.name} меньше или равна средней прибыли")
    else:
        print(f"Прибыль компании {c.name} больше средней прибыли")
