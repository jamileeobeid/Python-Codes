import time

def linearSearch(arr, target):

    for i in range(len(arr)):

        if arr[i] == target:
            return i
        
    return None

def main():

    start = time.perf_counter()

    arr = [10, 20, 30, 40, 50]
    target = 40
    result = linearSearch(arr, target)

    if result != None:
        print("target found at index:", result)
    
    else:
        print("target not found")

    end = time.perf_counter()

    time_taken = end - start
    print("Timetaken =", time_taken)

main()