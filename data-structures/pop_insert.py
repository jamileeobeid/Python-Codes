a_list = ["a", "b", "c", "d", "e"]
a = a_list.pop(0) 
print(a) # a
e = a_list.pop() 
print(e) # e
c = a_list.pop()  
print(c) # d

print(a_list) # ["b", "c"]




b_list = [2, 3]
b_list.insert(0, 1)
b_list.insert(2, 4)
b_list.insert(3, 4)  
print(b_list) #[1, 2, 4, 4, 3]