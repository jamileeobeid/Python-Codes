#Quick sort
def quick_sort(arr):

    # BASE CASE
    if len(arr) <= 1:
        return arr

    # Choosing a pivot (middle element)
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]

    # Partition the list into elements less than or equal to the pivot
    less = [x for x in arr[:pivot_index] + arr[pivot_index + 1:] if x <= pivot]

    # Partition the list into elements greater than the pivot
    greater = [x for x in arr[:pivot_index] + arr[pivot_index + 1:] if x > pivot]

    # Recursively apply quick sort
    return quick_sort(less) + [pivot] + quick_sort(greater)
