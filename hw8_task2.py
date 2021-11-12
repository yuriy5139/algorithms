"""
2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
которые необходимо обойти.
"""

from collections import namedtuple
from copy import copy

Vertex = namedtuple('Vertex', ['id', 'cost'])
g = {0: [Vertex(3, 1), Vertex(2, 1), Vertex(4, 9)],
     1: [Vertex(3, 4), Vertex(2, 9), Vertex(6, 7)],
     2: [Vertex(1, 9), Vertex(4, 3), Vertex(6, 7)],
     3: [],
     4: [Vertex(6, 1)],
     5: [Vertex(6, 1)],
     6: [Vertex(2, 6), Vertex(4, 8), Vertex(5, 5)],
     7: [Vertex(5, 1), Vertex(6, 2)]}

Route = namedtuple('Route', ['cost', 'hops'])


def process_ngbhrs(g, start,  current, routes, completed):
    if current in routes:
        curr_cost = routes[current].cost
    else:
        curr_cost = 0

    print(f"entering node {current}, curr_cost = {curr_cost}")

    for ngbh in sorted(g[current], key=lambda item: item.id):
        if (ngbh.id not in routes or routes[ngbh.id].cost > curr_cost + ngbh.cost) and ngbh.id != start:
            routes[ngbh.id] = Route(curr_cost + ngbh.cost, [])
            print(f"added route to {ngbh.id}: {routes[ngbh.id]}")
    completed.append(current)


src = 2
dst = 5
routes = {}
completed = []

process_ngbhrs(g, src, src, routes, completed)
idle_cycle = False
while not idle_cycle:
    idle_cycle = True
    this_cycle = copy(routes).keys()
    for vertex in this_cycle:
        if vertex not in completed:
            process_ngbhrs(g, src, vertex, routes, completed)
            idle_cycle = False
print(routes)
