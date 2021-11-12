"""
2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
которые необходимо обойти.
"""

from collections import namedtuple
from copy import copy

Vertex = namedtuple('Vertex', ['id', 'cost']) # вершина, будем использовать для построения графа
Route = namedtuple('Route', ['cost', 'hops']) # маршрут, будем использовать в алгоритме построения маршрутов

# Создадим граф, аналогичный показанному на лекции
g = {0: [Vertex(3, 1), Vertex(2, 1), Vertex(4, 9)],
     1: [Vertex(3, 4), Vertex(2, 9), Vertex(6, 7)],
     2: [Vertex(1, 9), Vertex(4, 3), Vertex(6, 7)],
     3: [],
     4: [Vertex(6, 1)],
     5: [Vertex(6, 1)],
     6: [Vertex(2, 6), Vertex(4, 8), Vertex(5, 5)],
     7: [Vertex(5, 1), Vertex(6, 2)]}



# функция определяет, есть ли у заданного узла соседи, и, если есть, вносит в словарь routes маршруты до них
def process_ngbhrs(g, start,  current, routes, completed):
    if current in routes:
        curr_cost = routes[current].cost
        curr_hops = routes[current].hops
    else:
        curr_cost = 0
        curr_hops = []

    curr_hops.append(current)
    print(f"entering node {current}, curr_cost = {curr_cost}")

    for ngbh in sorted(g[current], key=lambda item: item.id):
        # если встречаем вершину впервые
        if ngbh.id not in routes and ngbh.id != start:
            # используем полный срез для копии curr_hops[:], иначе все записи будут ссылаться на один маршрут
            routes[ngbh.id] = Route(curr_cost + ngbh.cost, curr_hops[:])
            print(f"added route to {ngbh.id}: {routes[ngbh.id]}")

        # если маршрут существует, но мы нашли маршрут с более низкой стоимостью
        if ngbh.id in routes and routes[ngbh.id].cost > curr_cost + ngbh.cost and ngbh.id != start:
            routes[ngbh.id] = Route(curr_cost + ngbh.cost, curr_hops[:])
            print(f"updated route to {ngbh.id}: {routes[ngbh.id]}")
    completed.append(current)


if __name__ == "__main__":
    src = 0 # стартовая вершина
    dst = 5 # вершина, к которой строим маршрут
    routes = {} # пустой словарь для маршрутов
    completed = [] # пустой список, куда будем добавлять пройденные вершины

    process_ngbhrs(g, src, src, routes, completed) # для корректного старта нам нужна хотя бы одна запись в routes

    # запускаем цикл обработки графа. Он завершится, если на протяжении цикла мы прошли по всем известным вершинам,
    # но не добавили ни одного нового маршрута
    idle_cycle = False
    while not idle_cycle:
        idle_cycle = True
        this_cycle = copy(routes).keys() # копируем, чтобы не изменить словарь в цикле, который идет по его ключам
        for vertex in this_cycle:
            if vertex not in completed:
                process_ngbhrs(g, src, vertex, routes, completed)
                idle_cycle = False
    if dst in routes:
        print(f"\nКратчайший маршрут между узлом {src} и узлом {dst}: {routes[dst]}")
    else:
        print("\nМаршрут не существует")
