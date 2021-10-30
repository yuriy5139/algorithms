"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
"""
"""
Ответ: в такой формулировке задачи - никакие. 
Проверка:
"""
for i in range(2, 100):
    # проверяем, что исследуемое число делится на все числа из диапазона от 2 до 9
    marker = True
    numbers = range(2, 10)
    for j in numbers:
        if i % j != 0:
            marker = False
            break
    if marker: print("Число {} разделилось на все числа {}!".format(i, [num for num in numbers]))

"""
Если же искать максимальное число из диапазона от 2 до 99, которое кратно _максимальному_количеству_ чисел из 
диапазона от 2 до 9, это можно сделать так: 
"""
counter = {k: [] for k in range(2, 100)}

for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            counter[i].append(j)

# выведем 10 лидеров
for item in sorted(counter.items(), key=lambda item: len(item[1]), reverse=True)[:10]:
    print(item)
