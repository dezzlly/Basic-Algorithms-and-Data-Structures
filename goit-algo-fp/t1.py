class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Функция для создания односвязного списка из массива
def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Функция для печати списка
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# 1. Реверсирование списка
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# 2. Сортировка вставками
def insertion_sort(head):
    sorted_head = None
    current = head
    while current:
        next_node = current.next
        sorted_head = insert_sorted(sorted_head, current)
        current = next_node
    return sorted_head

def insert_sorted(head, node):
    if not head or node.value < head.value:
        node.next = head
        return node
    current = head
    while current.next and current.next.value < node.value:
        current = current.next
    node.next = current.next
    current.next = node
    return head

# 3. Объединение двух отсортированных списков
def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy
    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next

# Тестирование
if __name__ == "__main__":
    print("Создание списка:")
    list1 = create_linked_list([4, 2, 1, 3])
    print_linked_list(list1)

    print("\nРеверс списка:")
    reversed_list = reverse_list(list1)
    print_linked_list(reversed_list)

    print("\nСортировка списка:")
    sorted_list = insertion_sort(reversed_list)
    print_linked_list(sorted_list)

    print("\nОбъединение с другим отсортированным списком:")
    list2 = create_linked_list([0, 5, 6])
    merged = merge_sorted_lists(sorted_list, list2)
    print_linked_list(merged)
