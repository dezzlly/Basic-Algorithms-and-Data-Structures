import heapq

def min_connection_cost(cables):
    heapq.heapify(cables)  # Преобразуем список в мин-кучу
    total_cost = 0

    while len(cables) > 1:
        # Извлекаем два самых коротких кабеля
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first + second
        total_cost += cost

        # Добавляем обратно объединённый кабель
        heapq.heappush(cables, cost)

    return total_cost

# Пример:
cables = [4, 3, 2, 6]
print("Минимальные затраты на соединение:", min_connection_cost(cables))
