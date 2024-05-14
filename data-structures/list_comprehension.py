#list comprehension is a powerful alternative to creating a list that conatins a specific value

print([x for x in range(2,11)]) 
print([char for char in "DAZAI"])
print([x for x in range(0,20,2)])
print([char for char in "TOKYO"])
print([2 for _ in range(4)])




rows, cols = (3, 2)
arr = [[0]*cols]*rows

arr[0]=[1,1,1] #overwriting the first row 


#Iterating over all elemnts
for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()
