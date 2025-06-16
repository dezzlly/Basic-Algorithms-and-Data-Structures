# Узел дерева
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Функция для подсчета суммы всех значений
def sum_tree(node):
    if node is None:
        return 0
    return node.key + sum_tree(node.left) + sum_tree(node.right)

# Пример
if __name__ == "__main__":
    # Пример дерева:
    #       10
    #      /  \
    #     5   20
    #    / \
    #   2   7

    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.left.left = Node(2)
    root.left.right = Node(7)

    print("Сума всіх значень у дереві:", sum_tree(root))
