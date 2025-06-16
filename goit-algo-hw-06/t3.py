import heapq

# Граф с весами
graph = {
    "Анна": {"Богдан": 2, "Виктор": 1, "Елена": 5},
    "Богдан": {"Анна": 2, "Галина": 3},
    "Виктор": {"Анна": 1, "Дмитрий": 4},
    "Галина": {"Богдан": 3, "Дмитрий": 2},
    "Дмитрий": {"Виктор": 4, "Галина": 2, "Елена": 1},
    "Елена": {"Анна": 5, "Дмитрий": 1}
}

def dijkstra(graph, start):
    # Инициализация расстояний
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_nodes = {}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

# Функция для восстановления пути
def reconstruct_path(previous_nodes, start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = previous_nodes.get(current)
        if current is None:
            return None  # Нет пути
    path.append(start)
    path.reverse()
    return path

# Пример: запустить для каждой вершины
for node in graph:
    distances, previous_nodes = dijkstra(graph, node)
    print(f"\nКратчайшие пути от '{node}':")
    for target in graph:
        if node != target:
            path = reconstruct_path(previous_nodes, node, target)
            print(f"{node} -> {target}: путь {path}, длина {distances[target]}")
