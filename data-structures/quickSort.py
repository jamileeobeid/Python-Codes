# Best Case: O(nlogn)
# Typical Case: O(nlogn)
# Worse Case: O(n**2)

# O(nlogn) is faster than On**2

def quick_sort(arr):

    length = len(arr) #saving length of the array in a variable

    #BASE CASE
    if length <= 1:
        return arr 
    
    #finding the pivot
    pivot = arr[length//2]

    #finding the values less than the pivot
    less = [x for x in arr if x < pivot]

    #findng the values equal to the pivot
    equal = [x for x in arr if x == pivot]

    #finding the values more than the pivot
    more = [x for x in arr if x > pivot]


    #returning the sorted order
    return quick_sort(less) + equal + quick_sort(more)

array1 = [20, 10, 6, 16, 2, 4]
print("Array before quick sort:", array1)
print("Array after quick sort:",quick_sort(array1))
