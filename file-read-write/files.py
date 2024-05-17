my_file = open("example.txt")

for line in my_file:
    length = len(line)
    print(length)

my_file.close()