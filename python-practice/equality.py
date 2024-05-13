a = 5
b = 5
c = 5.0

#Shallow Equality
result = a is b
print("Shallow equality of 5 and 5:", result) #True

result = a is c
print("Shallow equality of 5 and 5.0:", result) #False

print("\n")

#Deep Equality
result = (a == b)
print("Deep equality of 5 and 5:", result) #True

result = (a == c)
print("Deep equality of 5 and 5.0:", result) #True


d = 17
e = "Seventeen"
result = (d == e)
print(result) #False