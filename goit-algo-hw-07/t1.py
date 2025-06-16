# Узел дерева
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Функция для поиска наибольшего значения
def find_max(node):
    if node is None:
        return None

    current = node
    # В BST/AVL наибольшее значение — в крайнем правом узле
    while current.right:
        current = current.right
    return current.key

# Пример
if __name__ == "__main__":
    # Пример дерева:
    #       10
    #      /  \
    #     5   20
    #         / \
    #        15  30

    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(30)

    print("Найбольшее значення у дереві:", find_max(root))
