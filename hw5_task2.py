"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
"""

from collections import deque
from abc import abstractmethod

dig = {str(i): i for i in range(10)}
dig.update({"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15})
letter = {v: k for k, v in dig.items()}


class Hex:

    @abstractmethod
    def equalize(a, b, left=True):
        a, b = a.copy(), b.copy()
        if len(a) > len(b):
            for i in range(len(a) - len(b)):
                b.appendleft("0") if left else b.append("0")
        elif len(b) > len(a):
            for i in range(len(b) - len(a)):
                a.appendleft("0") if left else a.append("0")
        return a, b

    def __init__(self, chars):
        self.num = deque()
        if isinstance(chars, str):
            self.num = deque(chars)
        if isinstance(chars, deque):
            self.num = chars
        if isinstance(chars, Hex):
            self.num = chars.num

    def __repr__(self):
        return ''.join(d for d in self.num)

    def __add__(self, other):
        s, o = Hex.equalize(self.num.copy(), other.num.copy())
        result = deque()
        mem = 0

        while s and o:
            ds, do = dig[s.pop()], dig[o.pop()]
            summ = ds + do + mem
            if summ <= 15:
                mem = 0
                result.appendleft(letter[summ])
            else:
                mem = 1
                result.appendleft(letter[summ - 16])

        if mem:
            result.appendleft("1")

        return Hex(result)

    def __mul__(self, other):
        if len(self.num) >= len(other.num):
            a, b = self.num.copy(), other.num.copy()
        else:
            a, b = other.num.copy(), self.num.copy()

        total = []
        while b:
            result = deque()
            db = dig[b.pop()]
            mem = 0
            a_ = a.copy()
            while a_:
                da = dig[a_.pop()]
                mltp = da * db + mem
                result.appendleft(letter[mltp % 16])
                mem = mltp // 16
            if mem:
                result.appendleft(letter[mem])
            total.append(result)

        mult_res = Hex("0")

        for i, num in enumerate(total):
            mult_res = mult_res + Hex(Hex.equalize(num, deque(['0' for i in range(len(num) + i)]), left=False)[0])

        return mult_res


num1 = Hex("C4F")
num2 = Hex("A2")
num3 = Hex("BBA")

print(f"Сумма чисел {num1} и {num2} равна {num1 + num2}")
print(f"Сумма чисел {num1}, {num2} и {num3} равна {num1 + num2 + num3}")
print(f"Произведение чисел {num1} и {num2} равно {num1 * num2}")
print(f"Произведение чисел {num1}, {num2} и {num3} равно {num1 * num2 * num3}")
