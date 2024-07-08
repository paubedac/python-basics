def insertion_sort(array):
    size = len(array)

    if size < 2:
        return array

    for i in range(1, size):
        key_item = array[i]
        j = i - 1

        while j >= 0 and array[j] > key_item:
                array[j + 1] = array[j]
                j -= 1

        array[j] = key_item

    return array