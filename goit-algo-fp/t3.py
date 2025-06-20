import heapq

def dijkstra(graph, start):
    # Инициализация
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Пропускаем устаревшие записи
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Если найден более короткий путь
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Пример графа
# Граф представлен как словарь: вершина -> список (сосед, вес)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

if __name__ == "__main__":
    start_vertex = 'A'
    shortest_paths = dijkstra(graph, start_vertex)

    print(f"Кратчайшие расстояния от вершины {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"{vertex}: {distance}")
