def BinarySearch(arr, start, end, target):

    if start > end:
        return None
    
    middle_index = (start + end) // 2

    if target < arr[middle_index]:
        return BinarySearch(arr, start, middle_index - 1, target)
    
    elif target > arr[middle_index]:
        return BinarySearch(arr, middle_index + 1, end, target)
    
    else:
        return middle_index

def main():
    arr = [10, 20, 30, 40, 50, 60]
    target = 30

    result = BinarySearch(arr, 0, len(arr) - 1, target)

    if result is not None:
        print("Target found at index:", result)
    else:
        print("Target not found")

if __name__ == "__main__":
    main()
