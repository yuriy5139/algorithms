"""
Задание 3
Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""

import random


# генератор графа
# по заданию граф без петель, но не без циклов!
def create_g(vert):
    g = {}
    vertexes = [i for i in range(vert)]
    for v in vertexes:
        # путь связи с другими вершинами создаются случайно, но не менее трех связей и не более количества узлов -2
        # так как граф без петель, связей вершин с самими собой нет
        others = vertexes[:]
        others.remove(v)
        edges = random.sample(others, random.randint(3, len(others)-3))
        g[v] = edges
    return g

# алгоритм поиска в глубину
# возвращает стоимости маршрутов до всех возможных узлов из заданного узла
# граф невзвешенный, поэтому стоимость - это количество пройденных ребер до нужной вершины.
# попробуем рекурсивный алгоритм. Останавливать рекурсивный поиск будем, если натыкаемся на вершину, через которую
# уже проходили в текущей рекурсии (т.е., при попадании в цикл)
def dfs(g, start, current, routes, curr_hops = None):

    if not curr_hops:
        curr_hops = []
    else:
        curr_hops = curr_hops[:]

    if current in routes:
        curr_cost = routes[current]
    else:
        curr_cost = 0

    for nghbr in g[current]:
        if nghbr in curr_hops:
            return
        if (nghbr not in routes or curr_cost + 1 < routes[nghbr]) and nghbr != start:
            routes[nghbr] = curr_cost + 1
            curr_hops.append(nghbr)
            dfs(g, start, nghbr, routes, curr_hops)


if __name__ == "__main__":
    # Если хотите генерировать граф:
    g = create_g(12)

    # Если хотите использовать отладочный граф для проверки:
    # g = {0: [1, 2, 3],
    #      1: [4, 5],
    #      2: [4, 6, 7],
    #      3: [6, 7],
    #      4: [0, 8],
    #      5: [4, 8],
    #      6: [7, 8],
    #      7: [3, 6, 9],
    #      8: [7, 6, 9],
    #      9: []}

    print("Работаем с графом ", g)
    start = 0
    routes = {}
    dfs(g, start, start, routes)
    print(f"Из узла {start} получены следующие маршруты:")
    for k, v in routes.items():
        print(f"к узлу {k} стоимость {v}")