from merge_sort import merge

def modified_insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    for i in range(left + 1, right + 1):
        key_item = array[i]
        j = i - 1

        while j >= left and array[j] > key_item:

            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array

def timsort(array):
    min_run = 32
    n = len(array)
    if n < 2:
        return array
    
    for i in range(0, n, min_run):
        modified_insertion_sort(array, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))

            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])

            array[start:start + len(merged_array)] = merged_array

        size *= 2

    return array