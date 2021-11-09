"""
Рассматриваемая задача на предмет подсчета памяти:

1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
"""

import sys
import platform

print("\nО системе:")
print(sys.version)
print(platform.platform())
print("-" * 80)

"""
На моей системе вывод такой:
3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)]
Windows-10-10.0.19041-SP0
"""


# Функция - счетчик
def memcalc(vars):
    print("\nСводка об использовании памяти:")
    total = 0
    for k, v in vars.items():
        print(f"\t--переменная {k} имеет тип {type(v).__name__} и использует {sys.getsizeof(v)} байт")
        total += sys.getsizeof(v)
    print(f"  Общий объем используемой памяти равен {total} байт\n")


# Реализация 1 - вложенный цикл и сохранение счетчика в словарь и использованием целочисленного деления
def implementation1():
    multiplicity = {}
    range2_100 = range(2, 100)
    range2_10 = range(2, 10)

    for num in range2_100:
        for divisor in range2_10:
            if num % divisor == 0:
                if divisor in multiplicity:
                    multiplicity[divisor] += 1
                else:
                    multiplicity[divisor] = 1
    for k, v in multiplicity.items():
        print(f"Числу {k} кратны {v} чисел в диапазоне от 2 до 99")

    return vars()


# Реализация 2 - вложенный цикл с сохранением результата в словарь и проверкой на превышение границы
def implementation2():
    range2_10 = range(2, 10)
    multiplicity = {k: 0 for k in range2_10}
    for num in range2_10:
        i = 1
        while num * i <= 99:
            multiplicity[num] += 1
            i += 1
    for k, v in multiplicity.items():
        print(f"Числу {k} кратны {v} чисел в диапазоне от 2 до 99")

    return vars()


# Реализация 3. Создадим словарь со списками в значениях.
# Каждый список будет содержать конкретные числа, которые делится данное число
# Чтобы получить ответ, просто выведем длину списка

def implementation3():
    range2_10 = range(2, 10)
    range2_100 = range(2, 100)
    numbers = {number: [] for number in range2_10}
    for number in range2_10:
        for n in range2_100:
            if n % number == 0:
                numbers[number].append(n)

    for k, v in numbers.items():
        print(f"Числу {k} кратны {len(v)} чисел в диапазоне от 2 до 99")

    return vars()


if __name__ == "__main__":
    implementations = [implementation1, implementation2, implementation3]
    for impl in implementations:
        print("Выполняем реализацию", impl.__name__)
        memcalc(impl())

"""
Вывод: реализация 1 использует на 48 байт больше памяти, так как в ней вместо цикла while используется
for, который требует range. Реализация 2 использует while, поэтому она экономит 48 байт и использует 520 байт вместо
568. 
Реализация implementation3 менее эффективна с точки зрения памяти, чем первые две, так как сохраняет не только счетчики, 
но и сами значения чисел, делимых на данное, в словарь. Вычитывая данные из словаря, мы имеем дело со списками, которые
приходится сохранять в переменную v типа list, занимающую 184 байт. В результате реализация 3 дает суммарное использование памяти
724 байт. 
"""
