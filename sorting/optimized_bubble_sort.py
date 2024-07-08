def optimized_bubble_sort(array):
    size = len(array)
    
    if size < 2:
        return array

    for i in range(size):
        is_sorted = True
        for j in range(size - i - 1):
            if array[j] > array[i]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_sorted = False

        if is_sorted:
            break

    return array