"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

list1 = [random.randint(0, 100) for i in range(20)]
max_el, min_el = list1[0], list1[0]
max_id, min_id = 0, 0

for i, elem in enumerate(list1):
    if elem > max_el:
        max_el = elem
        max_id = i
    if elem < min_el:
        min_el = elem
        min_id = i

print("Исходный массив: \n", list1)
print(f"\nНаибольший элемент {max_el} находится в позиции {max_id}, "
      f"наименьший элемент {min_el} находится в позиции {min_id}")

list1[min_id] = max_el
list1[max_id] = min_el
print("\nМеняем наибольший и наименьший элементы местами: \n", list1)
