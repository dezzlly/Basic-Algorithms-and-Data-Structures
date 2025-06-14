import random
import timeit

# Сортировка вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Сортировка слиянием
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

# Генерация случайных данных
def generate_data(size):
    return [random.randint(0, 10000) for _ in range(size)]

# Обёртки для timeit
def test_insertion():
    arr = generate_data(1000)
    insertion_sort(arr)

def test_merge():
    arr = generate_data(1000)
    merge_sort(arr)

def test_timsort():
    arr = generate_data(1000)
    sorted(arr)

# Измерение времени выполнения
print("Insertion Sort:", timeit.timeit(test_insertion, number=10))
print("Merge Sort:", timeit.timeit(test_merge, number=10))
print("Timsort (sorted):", timeit.timeit(test_timsort, number=10))
