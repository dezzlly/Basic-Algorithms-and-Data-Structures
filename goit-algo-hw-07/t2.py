# Узел дерева
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Функция для поиска наименьшего значения
def find_min(node):
    if node is None:
        return None

    current = node
    # В BST/AVL наименьшее значение — в крайнем левом узле
    while current.left:
        current = current.left
    return current.key

# Пример
if __name__ == "__main__":
    # Пример дерева:
    #       10
    #      /  \
    #     5   20
    #    /
    #   2

    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(2)
    root.right = Node(20)

    print("Найменше значення у дереві:", find_min(root))
