import pulp

# Создаем задачу на максимизацию
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Переменные: количество лимонада (x) и фруктового сока (y)
x = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
y = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Целевая функция: максимизируем общее количество напитков
model += x + y, "Total_Drinks"

# Ограничения по ресурсам
model += 2 * x + 1 * y <= 100, "Water_Constraint"
model += 1 * x <= 50, "Sugar_Constraint"
model += 1 * x <= 30, "Lemon_Juice_Constraint"
model += 2 * y <= 40, "Fruit_Puree_Constraint"

# Решаем задачу
model.solve()

# Вывод результатов
print("Решение:")
print(f"Лимонад: {x.varValue} ед.")
print(f"Фруктовый сок: {y.varValue} ед.")
print(f"Общее количество напитков: {pulp.value(model.objective)}")
