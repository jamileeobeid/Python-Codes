"""Write a Python function that takes a list of strings as input
 and returns a new list containing only the strings with more than three characters."""

a_list = ["Hello", "December", "Re", "AD", "Nana"]
new_list = []

for element in a_list:

    if len(element) > 3:
        new_list.append(element)

print(new_list)



#overwriting the b_list
a_list = ["a"]
b_list = ["b"]
b_list = a_list + b_list

print(b_list) #["a","b"]
   
b_list = b_list + [1, 2, 3]

print(b_list) # ["a","b",1, 2, 3]