#Non-destructive sorting (not in-place sorting)
a_list = [2, 1, 5, 4, 6]
b_list = sorted(a_list)
print("Non-Destructive:")
print(a_list)
print(b_list)


#Destructive sorting (in-place sorting)
a_list = [2, 1, 5, 4, 6]
a_list.sort()
print("Destructive")
print(a_list)


#Destructive sorting (in-place sorting)
a_list = ['c', 'a', 'b', 'v', 'k']
a_list.sort()
print(a_list)


#Captial letters are sorted before small letters
a_list = ['c', 'a', 'Z', 'V', 'k']
a_list.sort()
print(a_list)


#Making lowercase letters appear before uppercase letters
a_list = ['c', 'a', 'Z', 'V', 'k']
a_list.sort(key= str.lower)
print(a_list)


#how to sort in descending order
numbers = [45, 7, 6, 12, 2, 90]
sorted_list = sorted(numbers, reverse = True)
print(sorted_list)