# Best Case: O(n)
# Typical Case: O(n**2)
# Worse Case: O(n**2)

def insertion_sort(arr):

    for i in range(1, len(arr)):

        j = i

        while arr[j-1] > arr[j] and j > 0:

            arr[j-1], arr[j] = arr[j], arr[j-1]
            j = j - 1

arr = [5, 4, 3, 6, 1, 2]
insertion_sort(arr)
print(arr)