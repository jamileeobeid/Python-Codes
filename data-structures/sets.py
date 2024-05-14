a = {1, 2, 3, 4, 5}
b = {3, 4}

result = a.issuperset(b)
print(result) #True

result = b.issubset(a)
print(result) #True

c = {'a', 'b', 'c', 'd'}
d = {'x', 'y', 'z'}

result = c.union(d)
print(result) #{'c', 'a', 'z', 'x', 'b', 'y', 'd'}

e = {'a', 'b', 'c', 'd'}
f = {'b', 'c'}

result = e.intersection(f)
print(result) #{'b', 'c'}