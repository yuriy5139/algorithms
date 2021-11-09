import sys
import platform

"""
Рассматриваемая задача на предмет подсчета памяти:

1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
"""

print("-" * 80)
print("О системе:")
print(sys.version)
print(platform.platform())
print("-" * 80)

"""
На моей системе вывод такой:
3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)]
Windows-10-10.0.19041-SP0
"""


# Счетчик памяти
def memcalc(vrs, level=0, debug=False):
    total = 0
    indent = " " * 4 * level + "->"
    total += sys.getsizeof(vrs)
    if debug: print(f"{indent}Уровень{level} На входе переменная типа {type(vrs).__name__}, {sys.getsizeof(vrs)} байт")
    if isinstance(vrs, list):
        if debug: print(f"{indent}Уровень{level} Заходим в список")
        for item in vrs:
            level += 1
            total += memcalc(item, level=level, debug=debug)
            level -= 1
            if debug: print(f"{indent}Уровень{level} Прибавили элемент списка, теперь total равен", total)
        if debug: print(f"{indent}Уровень{level} Вышли из списка, total равен", total)
    elif isinstance(vrs, dict):
        if debug: print(f"{indent}Уровень{level} Заходим в словарь")
        for val in vrs.values():
            level += 1
            total += memcalc(val, level=level, debug=debug)
            level -= 1
            if debug: print(f"{indent}Уровень{level} Прибавили элемент словаря, теперь total равен", total)
        if debug: print(f"{indent}Уровень{level} Вышли из словаря, total равен", total)
    return total


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

    print(f"В реализации используются следующие переменные {vars()}")
    return list(vars().values())


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

    print(f"В реализации используются следующие переменные {vars()}")
    return list(vars().values())


# Реализация 3. Создадим словарь со списками в значениях.
# Каждый список будет содержать конкретные числа, которые делятся на данное число
# Чтобы получить ответ, будем использовать длину списка

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

    print(f"В реализации используются следующие переменные {vars()}")
    return list(vars().values())


if __name__ == "__main__":

    # Если выставить в True,
    # в функции memcalc() будет массивный вывод в консоль!
    DEBUG = False

    implementations = [implementation1, implementation2, implementation3]
    for impl in implementations:
        print("\n *** Проверяем реализацию", impl.__name__)
        print(f"Общий объем используемой памяти равен {memcalc(impl(), debug=DEBUG)} байт")

"""
Вывод:
По сравнению с реализацией 1, реализация 2 использует цикл while, который не требует range, поэтому она требует меньше памяти 
и является оптимальной. Реализация 3 хранит в списках все числа, которые делятся на данные. Хранение списков со значениями неэффективно,
так как и сами списки занимают память, и каждое значение int  в списке требует дополнительные 28 байт. 
Таким образом, реализация 3 является самой неэффективной, но зато она позволяет вывести все числа, кратные интересующим.
Реализация 1 и Реализация 2 хранят только количества, но не сами числа.
"""
