def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

array = [19, 13, 6, 2, 18, 8]
bubble_sort(array)
print(array)