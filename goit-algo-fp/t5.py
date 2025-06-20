import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Узел дерева
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.color = "#CCCCCC"
        self.id = str(uuid.uuid4())

# Строим дерево из массива-кучи
def build_heap_tree(heap):
    nodes = [Node(val) for val in heap]
    for i in range(len(nodes)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(nodes):
            nodes[i].left = nodes[left]
        if right < len(nodes):
            nodes[i].right = nodes[right]
    return nodes[0] if nodes else None

# Обход в ширину (BFS)
def bfs_color(root):
    queue = deque([root])
    visited = []
    while queue:
        node = queue.popleft()
        visited.append(node)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    apply_colors(visited)

# Обход в глубину (DFS)
def dfs_color(root):
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        visited.append(node)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    apply_colors(visited)

# Применение градиентной раскраски
def apply_colors(nodes):
    base_color = (18, 150, 240)  # #1296F0
    n = len(nodes)
    for i, node in enumerate(nodes):
        factor = int(100 + (155 * i / max(n-1, 1)))  # от тёмного к светлому
        r = min(255, int(base_color[0] * factor / 255))
        g = min(255, int(base_color[1] * factor / 255))
        b = min(255, int(base_color[2] * factor / 255))
        node.color = f'#{r:02x}{g:02x}{b:02x}'

# Добавление узлов и рёбер
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, label=node.val, color=node.color)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, l, y - 1, layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, r, y - 1, layer + 1)

# Отрисовка дерева
def draw_tree(root, title):
    G = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(G, root, pos)

    colors = [G.nodes[n]['color'] for n in G.nodes()]
    labels = {n: G.nodes[n]['label'] for n in G.nodes()}

    plt.figure(figsize=(8, 5))
    nx.draw(G, pos, labels=labels, node_color=colors,
            node_size=2500, arrows=False, font_size=12)
    plt.title(title)
    plt.show()

# --- Запуск программы ---
if __name__ == "__main__":
    heap_array = [0, 4, 1, 5, 10, 3]

    # BFS
    root_bfs = build_heap_tree(heap_array)
    bfs_color(root_bfs)
    draw_tree(root_bfs, "Обход в ширину (BFS)")

    # DFS
    root_dfs = build_heap_tree(heap_array)
    dfs_color(root_dfs)
    draw_tree(root_dfs, "Обход в глубину (DFS)")
