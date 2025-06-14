import networkx as nx
import matplotlib.pyplot as plt

# Создаем пустой граф
G = nx.Graph()

# Добавляем вершины (люди)
people = ["Анна", "Богдан", "Виктор", "Галина", "Дмитрий", "Елена"]
G.add_nodes_from(people)

# Добавляем связи (дружба между людьми)
edges = [
    ("Анна", "Богдан"),
    ("Анна", "Виктор"),
    ("Богдан", "Галина"),
    ("Галина", "Дмитрий"),
    ("Виктор", "Дмитрий"),
    ("Дмитрий", "Елена"),
    ("Елена", "Анна")
]
G.add_edges_from(edges)

# Визуализируем граф
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, font_size=12)
plt.title("Социальная сеть")
plt.show()

# Анализ характеристик графа
print(f"Количество вершин: {G.number_of_nodes()}")
print(f"Количество рёбер: {G.number_of_edges()}")

# Степени вершин
print("\nСтепень каждой вершины:")
for node, degree in G.degree():
    print(f"{node}: {degree}")
