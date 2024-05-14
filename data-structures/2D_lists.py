array= [[1,2,3], [4,5,6], [7,8,9]]
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
print(array[1][2]) #6



# iterate through all the elements of a 2 dimensional list

for row in array:
    for element in row:
        print(element, end = ' ')
    print() #prints each row in a row



rows, cols= (3,3)
arr= [[0] *cols]* rows
print(arr) #[[0, 0, 0], [0, 0, 0], [0, 0, 0]]



row, cols = (3, 2)
arr = [[2]*cols]*rows
#2 2
#2 2
#2 2

arr[0] = [1, 2, 3] #overwriting the first column 
for row in arr:
    for element in row:
        print(element, end = ' ')
    print()
#1 2 3 
#2 2
#2 2

array= [[1,2,3], [4,5,6], [7,8,9]]
print(array) #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(array[1][2]) #6
array[1][2]= 7
print(array[1][2]) #7

rows, cols= (3,3)
arr=[[0]* cols]* rows
print(arr) #7

#iterating over the rows and columns using nested loop
for row in array:
    for element in row:
        print(element, end=" ")
    print() #[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    

array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(array)


#Accessing index value
print(array[1][2])


rows, cols = (3, 3)
arr = [[0]*cols]*rows
arr[1]=[3,3]


# Iterating over all elemnts
for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()