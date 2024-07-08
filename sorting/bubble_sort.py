def bubble_sort(array):
    size = len(array)
    
    if size < 2:
        return array

    for i in range(size):
        for j in range(size - i - 1):
            if array[j] > array[i]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    return array