def swap():

    a = 6
    b = 7

    print("a before swapping:", a)
    print("b before swapping:", b)

    print("\n")

    temp = a
    a = b
    b = temp

    print("a after swapping:", a)
    print("b after swapping:", b)   

swap() 

print("\n")

# swapping first half of the list with the second half of the list
numbers = [1, 2, 3, 4, 5, 6]
print("Before swapping first and second half:", numbers)
numbers[:3], numbers[3:] = numbers[3:], numbers[:3]
print("After swapping first and second half:", numbers)