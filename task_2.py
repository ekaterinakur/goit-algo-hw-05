def binary_search(array, target):
    low = 0
    high = len(array) - 1
    iterations = 0

    upper_limit = None

    while low <= high:
        mid = (low + high) // 2
        mid_value = array[mid]

        iterations += 1

        if mid_value == target:
            upper_limit = mid_value
            return iterations, upper_limit
        elif mid_value < target:
            low = mid + 1
        else:
            upper_limit = mid_value
            high = mid - 1

    return iterations, upper_limit

sorted_arr = [0.1, 0.4, 1.2, 1.8, 2.3, 3.0, 4.5, 5.1]
target = 2.3

iterations, upper_limit = binary_search(sorted_arr, target)

if upper_limit is not None:
    print(f"Кількість ітерацій: {iterations}")
    print(f"Верхня межа для {target}: {upper_limit}")
else:
    print(f"Елемента {target} немає в масиві.")
