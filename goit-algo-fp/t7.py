import random
import matplotlib.pyplot as plt

def monte_carlo_dice_simulation(num_rolls=100000):
    counts = {i: 0 for i in range(2, 13)}  # Суммы от 2 до 12

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        counts[total] += 1

    # Расчёт вероятностей
    probabilities = {k: round(v / num_rolls * 100, 2) for k, v in counts.items()}
    return counts, probabilities

def print_table(counts, probabilities, num_rolls):
    print(f"{'Сумма':^10} | {'Кол-во':^10} | {'Вероятность':^15}")
    print("-" * 40)
    for total in range(2, 13):
        count = counts[total]
        prob = probabilities[total]
        fraction = f"{count}/{num_rolls}"
        print(f"{total:^10} | {count:^10} | {prob:.2f}% ({fraction})")

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.figure(figsize=(8, 5))
    plt.bar(sums, probs, color="skyblue", edgecolor="black")
    plt.title("Monte Carlo: Вероятности сумм при броске двух кубиков")
    plt.xlabel("Сумма")
    plt.ylabel("Вероятность (%)")
    plt.xticks(range(2, 13))
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

# --- Запуск ---
if __name__ == "__main__":
    rolls = 100000
    counts, probabilities = monte_carlo_dice_simulation(rolls)
    print_table(counts, probabilities, rolls)
    plot_probabilities(probabilities)
