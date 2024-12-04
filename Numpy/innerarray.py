import numpy as np

N = int(input("Enter an integer: "))

random_array = np.random.randint(0, 100, (N, N))
print("random array:")
print(random_array)

if N > 2:
    inner_array = random_array[1:-1, 1:-1]
else:
    inner_array = np.array([])

print("inner array:")
print(inner_array)
