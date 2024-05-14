"""Write a Python function that takes two tuples,
 converts them to lists, swaps their values, 
 and then converts them back to tuples."""


numbers = (1, 2) #taking 2 tuples
print("numbers as tuples:", numbers)

a_list = list(numbers) #converting them to list
print("conversting numbers to lists:", a_list)

"""SWAPPING"""
temp = a_list[0]
a_list[0] = a_list[1]
a_list[1] = temp

print("Swapping the values in lists:", a_list)

new_numbers = tuple(a_list) #converting the swapped values back to tuples
print("swapped tuples:", new_numbers)



def nestedTuple(t):
    print(len(t)) #4
    print(t[3])
    


alphabets= (('a','b','1'),('d','e','f'), ('g','h','i'),True)
nestedTuple(alphabets)


import random

def tuples():
    nums= tuple(random.random() for _ in range(3))
    return nums

print(tuples())
