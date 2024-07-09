def heapify(array, size, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
 
    if l < size and array[i] < array[l]:
        largest = l
 
    if r < size and array[largest] < array[r]:
        largest = r
 
    if largest != i:
        (array[i], array[largest]) = (array[largest], array[i])
        heapify(array, size, largest)
 
def heap_sort(array):
    size = len(array)

    for i in range(size // 2, -1, -1):
        heapify(array, n, i)
  
    for i in range(size - 1, 0, -1):
        (array[i], array[0]) = (array[0], array[i])
        heapify(array, i, 0)

    return array