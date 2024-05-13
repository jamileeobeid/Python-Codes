countries = dict()
print(countries) #printing an empty dictionary

countries = {"Palestine": "Al-Quds", "Japan": "Tokyo", "Korea": "Seoul"}
print(countries)

#checking whether a key is in the dictionary
element = "Palestine"

if element in countries:
    print("Element is found")

else:
    print("Element is not found")


# printing all keys
keys = countries.keys()
print(keys)

#printing all values
values = countries.values()
print(values)

# appending 
countries["Lebanon"] = "Beirut"
print(countries)

# changing values
countries["Japan"] = "Shibuya"
print(countries)

# iterate over the dictionary items
for key in countries:
    values = countries[key]
    print(key,":",values)

# sorting keys
keys = countries.keys()
print(sorted(keys))

# sorting values
values = countries.values()
print(sorted(values))


# Creating KeyError by retrieving a value that doesn't exist
print(countries["UAE"])