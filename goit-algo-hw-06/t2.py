import networkx as nx
from collections import deque

# Граф из задания 1
G = nx.Graph()
people = ["Анна", "Богдан", "Виктор", "Галина", "Дмитрий", "Елена"]
edges = [
    ("Анна", "Богдан"),
    ("Анна", "Виктор"),
    ("Богдан", "Галина"),
    ("Галина", "Дмитрий"),
    ("Виктор", "Дмитрий"),
    ("Дмитрий", "Елена"),
    ("Елена", "Анна")
]
G.add_nodes_from(people)
G.add_edges_from(edges)

# DFS — Поиск пути в глубину
def dfs_path(graph, start, goal, path=None, visited=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [start]
    visited.add(start)

    if start == goal:
        return path

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            new_path = dfs_path(graph, neighbor, goal, path + [neighbor], visited)
            if new_path:
                return new_path
    return None

# BFS — Поиск пути в ширину
def bfs_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

# Используем алгоритмы
start_node = "Анна"
goal_node = "Дмитрий"

dfs_result = dfs_path(G, start_node, goal_node)
bfs_result = bfs_path(G, start_node, goal_node)

# Выводим результаты
print("DFS путь:", dfs_result)
print("BFS путь:", bfs_result)

# Объяснение
print("\nОбъяснение:")
print("DFS может идти по более длинному пути, потому что он идёт 'вглубь' сначала, не проверяя все короткие пути.")
print("BFS всегда находит кратчайший путь (в терминах количества рёбер), потому что проверяет все соседние вершины.")
