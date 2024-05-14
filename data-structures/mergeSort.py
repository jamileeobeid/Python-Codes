# Best Case: O(nlogn)
# Typical Case: O(nlogn)
# Worse Case: O(nlogn)

def merge_sort(arr):

    #merge sort only works if the length of the array is greater than 1
    if len(arr) > 1:

        #left side is from index 0 till middle
        left_side = arr[:len(arr)//2]

        #right side is from the middle until the end
        right_side = arr[len(arr)//2:]

        #using recursion on each side
        merge_sort(left_side)
        merge_sort(right_side)

        #merging 
        i = 0 #left most element in left side
        j = 0 #left most element in right side
        k = 0 #merged array index 

        while i < len(left_side) and j < len(right_side):

            if left_side[i] < right_side[j]:
                arr[k] = left_side[i] # saving the merged array index 
                 
                i = i + 1
                k = k + 1

            else:
                arr[k] = right_side[j] # saving the merged array index 
                 
                j = j + 1
                k = k + 1   

        # transferring missing elements from left side to merged array
        while i < len(left_side): 

            arr[k] = left_side[i]
            i = i + 1
            k = k + 1

        # transferring missing elements from right side to merged array
        while j < len(right_side): 

            arr[k] = right_side[j]
            j = j + 1
            k = k + 1

arr = [12, 20, 7, 6, 5, 18]
print("array before sorting:", arr)
merge_sort(arr)
print("array after sorting:", arr)