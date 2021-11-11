"""
2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
которые необходимо обойти.
"""

# копировать код преподавателя с экрана было неудобно - попробуем написать алгоритм самостоятельно :)
# будем работать с графом, который использовался на лекции

# В алгоритме нам придется обходить вершины и проверять пути до соседей. Это лучше сделать списками смежности.
# Т.е., нужно хранить для каждой вершины пару (номер связанной вершины, стоимость маршрута).

from collections import namedtuple, deque

Vertex = namedtuple('Vertex', ['id', 'cost'])
g = {0: [Vertex(3, 1), Vertex(2, 1), Vertex(4, 9)],
     1: [Vertex(3, 4), Vertex(2, 9), Vertex(6, 7)],
     2: [Vertex(1, 9), Vertex(4, 3), Vertex(6, 7)],
     4: [Vertex(6, 1)],
     5: [Vertex(6, 1)],
     6: [Vertex(2, 6), Vertex(4, 8), Vertex(5, 5)],
     7: [Vertex(5, 1), Vertex(6, 2)]}

# Кратчайший маршрут нужно искать из списка возможных, в каждом из которых есть вершина и стоимость до нее.
# При обходе графа помимо стоимости вершины будем сохранять путь, через который эта стоимость получена.

Routes = namedtuple('Routes', ['vertex_id', 'hops'])

src = 2
dst = 5

def get_routes(g, current, routes, to_visit, src):
    if current not in routes:
        curr_cost = 0
    else: curr_cost = routes[current]
    print(f"Зашел в узел {current}: routes = {routes}, to_visit = {to_visit}, curr_cost = {curr_cost}")
    if not to_visit:
        return
    if g[current]:
        nghbrs = sorted(g[current], key=lambda item: item.id)
        print(f"\tВижу соседей: {nghbrs}")
        for nghb in nghbrs:
            if (nghb.id not in routes or routes[nghb.id] > curr_cost + nghb.cost) and nghb.id != src:
                routes[nghb.id] = curr_cost + nghb.cost
                print(f"\tДобавил маршрут {nghb.id} со стоимостью {routes[nghb.id]}")

        to_visit.remove(current)
        for nghb in nghbrs:
            if nghb.id in to_visit:
                get_routes(g, nghb.id, routes, to_visit, src)
    else:
        print("Соседей нет")
        to_visit.remove(current)
        return


to_visit = sorted(g.keys())
routes = {}
get_routes(g, src, routes, to_visit, src)
print(routes)
