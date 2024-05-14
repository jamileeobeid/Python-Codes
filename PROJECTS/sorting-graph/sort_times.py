#importing time
import time 

#importing 'plotter.py' file
import plotter

#importing random
import random 

#importing merge sort
from merge_sort import merge_sort

#importing insertion sort
from insertion_sort import insertion_sort

#importing quick sort
from quick_sort import quick_sort

"""GLOBAL ARRAY"""
SIZES = [200, 500, 800, 1100, 1400, 1700, 2000]

#defining the function sort_function_timer
def sort_function_timer(sort_function, an_array):

    #Starting the timer
    begin = time.perf_counter()

    sort_function(an_array)

    #Ending the timer
    end = time.perf_counter()

    #Calculating the elapsed time [time taken]
    elapsed = end - begin

    #returning the elapsed time [time taken]
    return elapsed 

#defining the function plot_sort_time_using_random_arrays
def plot_sort_time_using_random_arrays(sort_function):

    """Timing how long it takes for a sorting function to sort random arrays of various sizes"""

    print("timing", sort_function.__name__)
    plotter.new_series()

    for size in SIZES:

        #Generating random arrays in range size from 1 to 2000
        random_array = [random.randint(1,2000) for _ in range(size)]
        
        # calling insertion, merge, and quick sort with one argument [array]
        if sort_function in [insertion_sort, merge_sort, quick_sort,quick_insertion_sort]:
            time_taken = sort_function_timer(sort_function, random_array)

        #adding the data points to the plot
        plotter.add_data_point(time_taken)

        #printing the time taken in seconds
        print("Time taken for size", size, "is", time_taken, "seconds")

#defining the plot_sort_time_using_sorted_z function
def plot_sort_time_using_sorted_z(sort_function):


    """Timing how long it takes for a sorting function to sort sorted arrays of various sizes"""

    print("timing", sort_function.__name__)
    plotter.new_series()

    for size in SIZES:

        #Generating sorted random arrays in range size from 1 to 2000
        random_array = [random.randint(1,2000) for _ in range(size)]
        random_array.sort()

        # calling insertion, merge, and quick sort with one argument [array]
        if sort_function in [insertion_sort, merge_sort, quick_sort,quick_insertion_sort]:
            time_taken = sort_function_timer(sort_function, random_array)

        #adding the data points to the plot
        plotter.add_data_point(time_taken)

        #printing the time taken in seconds
        print("Time taken for size", size, "is", time_taken, "seconds")

"""Now, we're going to check whether the array is sorted or nearly sorted.
This will help our quick_insertion_sort() function (hybrid code) to decided whether 
to switch to insertion sort or quick sort"""

def is_array_sorted(arr):   

    q = 1    #starting index q as 1 so that we compare it with previous elements  

    #continuing the while loop as long as the q is less that the length of the array
    while q < len(arr):   

        #comparing element at index q with the element at the previous index 
        if(arr[q] < arr[q - 1]): 

            #Will return false if Element at index "q" is less than the previous element 
            return False          
        q = q + 1

    #Will return True as the while loop will not find any unsorted elements    
    return True  


"""DEFINING THE FUNCTION FOR THE HYBRID CODE"""
#(combination of quick and insertion sort)
def quick_insertion_sort(an_array):    

    #using function is_array_sorted to check if its sorted
    if is_array_sorted(an_array) == False:  
        
        #BASE CASE
        if len(an_array) <2 :
            return an_array

        # Choosing a pivot (middle element)
        pivot_index = len(an_array) // 2
        pivot = an_array[pivot_index]

        # Partition the list into elements less than or equal to the pivot
        less = [x for x in an_array[:pivot_index] + an_array[pivot_index + 1:] if x <= pivot]

        # Partition the list into elements greater than the pivot
        greater = [x for x in an_array[:pivot_index] + an_array[pivot_index + 1:] if x > pivot]

        # Recursively apply quick sort
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
    else:
        
        #when array is sorted or nearly sorted, we're switching to insertion sort

        """DEFINING INSERTION SORT"""

        # storing the length of the array in 'n'
        n = len(an_array)
        
        #if length of the array is 1 or 0, that means it's sorted
        #therefore, we return the array
        if n <= 1:
            return an_array

        for i in range(1, n):
            key = an_array[i]
            j = i - 1

            while j >= 0 and key < an_array[j]:
                an_array[j + 1] = an_array[j]
                j -= 1
            an_array[j + 1] = key
    
        return an_array

"""CALLING FUNCTIONS FROM MAIN"""
def main():  

    #initializing the plot
    plotter.init("My Graph", "X-Axis", "Y-Axis")

    #calling 'plot_sort_time_using_random_arrays' 3 times using a different sort each time
    #plot_sort_time_using_random_arrays(insertion_sort)
    #plot_sort_time_using_random_arrays(merge_sort)
    #plot_sort_time_using_random_arrays(quick_sort)

    """CALLING HYBRID SORT FOR RANDOM ARRAYS"""
    #plot_sort_time_using_random_arrays(quick_insertion_sort)
    
    
    #calling 'plot_sort_time_using_sorted_z' 3 times using a different sort each time
    plot_sort_time_using_sorted_z(insertion_sort)
    plot_sort_time_using_sorted_z(merge_sort)
    plot_sort_time_using_sorted_z(quick_sort)

    """CALLING HYBRID SORT FOR SORTED ARRAYS"""
    plot_sort_time_using_sorted_z(quick_insertion_sort)

    
    #Displaying the plot
    plotter.plot()

    #keeping the window open until the user closes it 
    input("Press Enter to continue...")

main()