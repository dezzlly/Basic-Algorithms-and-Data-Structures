def binary_search_upper_bound(arr, target):
    left = 0
    right = len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    return (iterations, upper_bound)


arr = [1.2, 2.4, 3.1, 4.8, 5.5, 6.0, 7.3]
print(binary_search_upper_bound(arr, 4.0))  # (кількість ітерацій, 4.8)
print(binary_search_upper_bound(arr, 7.3))  # (кількість ітерацій, 7.3)
print(binary_search_upper_bound(arr, 8.0))  # (кількість ітерацій, None)
