items = {
    "pizza":     {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog":   {"cost": 30, "calories": 200},
    "pepsi":     {"cost": 10, "calories": 100},
    "cola":      {"cost": 15, "calories": 220},
    "potato":    {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    selected = []

    for name, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            total_cost += data['cost']
            total_calories += data['calories']
            selected.append(name)

    return selected, total_cost, total_calories

def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, data = item_list[i - 1]
        cost, calories = data['cost'], data['calories']
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Восстановление выбранных блюд
    w = budget
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, data = item_list[i - 1]
            selected.append(name)
            w -= data['cost']

    total_cost = sum(items[name]['cost'] for name in selected)
    total_calories = sum(items[name]['calories'] for name in selected)
    return selected[::-1], total_cost, total_calories

if __name__ == "__main__":
    budget = 100

    print("💡 Greedy Algorithm:")
    g_items, g_cost, g_cal = greedy_algorithm(items, budget)
    print(f"  Выбрано: {g_items}")
    print(f"  Общая стоимость: {g_cost}, Калории: {g_cal}")

    print("\n🔧 Dynamic Programming:")
    d_items, d_cost, d_cal = dynamic_programming(items, budget)
    print(f"  Выбрано: {d_items}")
    print(f"  Общая стоимость: {d_cost}, Калории: {d_cal}")
