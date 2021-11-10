"""
Задание 2

Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""

import random
from collections import deque


# вспомогательная функция - выполняет склейку с сортировкой двух половинок
def merge(left, right):
    d_right, d_left = deque(right), deque(left)
    result = []
    while d_left and d_right:
        if d_left[0] <= d_right[0]:
            result.append(d_left.popleft())
        else:
            result.append(d_right.popleft())
    result.extend(d_right) if d_right else result.extend(d_left)
    return result


# Реализация будет рекурсией. Будем разбивать список на равные половинки, их сортировать, а затем склеивать вместе
def merge_sort(lst=None, left=None, right=None, level=0, debug=False):
    indent = " " * level * 4
    if debug: print(f"{indent} level = {level}, lst = {lst}, left = {left}, right = {right}")

    # 1. Если доразбивались до массива из 1 элемента, возвращаем его - нечего сортировать
    if lst and len(lst) == 1:
        return lst

    # 2. Если еще есть, куда разбивать, разбиваем дальше
    if lst:
        l_index = len(lst) // 2
        left = lst[:l_index]
        right = lst[l_index:]
        level += 1
        return merge_sort(left=merge_sort(lst=left, level=level, debug=debug),
                          right=merge_sort(lst=right, level=level, debug=debug), level=level, debug=debug)

    # 3. Функцию вызвали без lst, значит - с left и right. Склеиваем
    return merge(left, right)


if __name__ == "__main__":
    # Если хотите смотреть дебаг рекурсии - выставьте в True
    debug = False

    lst = [i for i in range(0, 50)]
    random.shuffle(lst)
    print("Исходный массив:\n", lst)
    print("Отсортированный массив:\n", merge_sort(lst=lst, debug=debug))
