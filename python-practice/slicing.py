a_string = "Bungou Stray Dogs"

slicing = a_string[7:12] #taking 'Stray' from the above statement
print(slicing)


a_string = "Buttercup EIP"
doggo = list(a_string)

#printing portions of 'a_string' variable:

slice = doggo[2:6]
print(slice) # t t e r  

slice = doggo[:6]

print(slice) # B u t t e r

slice = doggo[:-4:-1]
print(slice) # P I E


my_list=[1,2,3,"apple", "banana"]
my_list[3]= "orange" #changing "apple" to "orange"

print(my_list)

sliced=my_list[1:4]
 #output: 2,3,"orange"
print(sliced)
