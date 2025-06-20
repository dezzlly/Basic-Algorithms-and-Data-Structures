# Набор монет
coins = [50, 25, 10, 5, 2, 1]

# Жадный алгоритм
def find_coins_greedy(amount):
    result = {}
    for coin in sorted(coins, reverse=True):
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

# Алгоритм динамического программирования
def find_min_coins(amount):
    # min_coins[i] будет хранить минимальное количество монет для суммы i
    min_coins = [float('inf')] * (amount + 1)
    # backtrack[i] будет хранить монету, использованную для достижения суммы i
    backtrack = [-1] * (amount + 1)
    min_coins[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                backtrack[i] = coin

    if min_coins[amount] == float('inf'):
        return {}  # Сумма не может быть собрана

    # Восстановление решения
    result = {}
    current = amount
    while current > 0:
        coin = backtrack[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result

# Пример
if __name__ == "__main__":
    amount = 113
    print("Greedy:", find_coins_greedy(amount))
    print("DP:", find_min_coins(amount))
