"""
Задание 1.
На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""

# Каждый друг может пожать руку каждому - это полносвязный граф.
# Одно рукопожатие - проход по маршруту из одной вершины в другую
# Чтобы решить задачу, построим граф по методу списка ребер. В списке ребер запрещено добавлять маршрут из 1 в 0,
# если маршрут из 0 в 1 уже добавлен - как раз то, что нужно. Для получения ответа просто посчитаем количество записей.

# Обозначим маршрут кортежем. Для проверки, что такого маршрута еще нет, будем всегда формирвоать маршрут по принципу
# от вершины с меньшим номером к вершине с большим номером.

FRIENDS = 10
g = set()
for i in range(FRIENDS):
    for j in range(FRIENDS):
        if i == j:
            continue
        g.add((i, j)) if i < j else g.add((j, i))
print(f"Количество рукопожатий между {FRIENDS} друзьями равно {len(g)}")
