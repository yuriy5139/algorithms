"""4. Определить, какое число в массиве встречается чаще всего."""

import random

list1 = [random.randint(1, 7) for i in range(40)]
print("Список: ", list1)

counter = {}
for el in list1:
    if el in counter:
        counter[el] += 1
    else:
        counter[el] = 1

for item in sorted(counter.items(), key=lambda item: item[1], reverse=True):
    print(f"Число {item[0]} встречается в списке {item[1]} раз")
