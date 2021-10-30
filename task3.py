"""
3. Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

import random
import re

a, b = input("введите через пробел начало и окончание диапазона ").split(' ')
if re.match(r'\d+\.\d+', a) and re.match(r'\d+\.\d+', b):
    print(random.uniform(float(a), float(b)))
elif re.match(r'\d+', a) and re.match(r'\d+', b):
    print(random.randint(int(a), int(b)))
elif re.match(r'[a-zA-Z]', a) and re.match(r'[a-zA-Z]', b):
    print(chr(random.randint(ord(a), ord(b))))