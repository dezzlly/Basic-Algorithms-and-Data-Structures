import networkx as nx

# Создание взвешенного графа
G = nx.Graph()
people = ["Анна", "Богдан", "Виктор", "Галина", "Дмитрий", "Елена"]
G.add_nodes_from(people)

# Добавим ребра с весами (например, "стоимость общения" или "расстояние")
edges_with_weights = [
    ("Анна", "Богдан", 2),
    ("Анна", "Виктор", 1),
    ("Богдан", "Галина", 3),
    ("Галина", "Дмитрий", 2),
    ("Виктор", "Дмитрий", 4),
    ("Дмитрий", "Елена", 1),
    ("Елена", "Анна", 5)
]

G.add_weighted_edges_from(edges_with_weights)

# Вывод кратчайших путей от каждой вершины
for source in G.nodes:
    print(f"\nКратчайшие пути от '{source}':")
    for target in G.nodes:
        if source != target:
            path = nx.dijkstra_path(G, source=source, target=target, weight='weight')
            distance = nx.dijkstra_path_length(G, source=source, target=target, weight='weight')
            print(f"{source} -> {target}: путь {path}, длина {distance}")
