"""4. Определить, какое число в массиве встречается чаще всего."""

import random
import numpy as np
import timeit

list1 = [random.randint(0, 20) for i in range(1000)]


# способ 1 - проходим однократно по массиву, встречу каждого числа запоминаем в словарь.
def solution1(lst):
    counter = {}
    for el in lst:
        if el in counter:
            counter[el] += 1
        else:
            counter[el] = 1
    return sorted(counter.items(), key=lambda item: item[1], reverse=True)[0]


# способ 2: получаем уникальные числа массива, преобразовав его в множесво. Дальше пользуемся функцией list.count()
def solution2(lst):
    unique = set(lst)
    max_elem = 0
    max_count = 0
    for item in unique:
        cnt = lst.count(item)
        if cnt > max_count:
            max_count = cnt
            max_elem = item
    return max_elem, max_count


# способ 3: преобразуем список в numpy-массив, дальше будем запускать для каждого
# уникального числа np.where и сравнивать по этому результату (аналогично предыдущему, но с nunpy)
def solution3(lst):
    lstn = np.asarray(lst)
    unique = set(lst)
    max_elem = 0
    max_count = 0
    for item in unique:
        cnt = np.where(lstn == item)[0]
        if len(cnt) > max_count:
            max_count = len(cnt)
            max_elem = item
    return max_elem, max_count


if __name__ == "__main__":
    for implementation in [solution1, solution2, solution3]:
        print(f"Время работы варианта {implementation.__name__}: "
              f"{timeit.timeit(stmt=lambda: implementation(list1), number=1000)}")
