#we will create a code that no matter the value of a and b,
#the smaller value will always be printed first

def print_first(comparator, a, b):

    if comparator(a,b):
        print(a,b)

    else:
        print(b,a)

def less_than(a, b):
    return a <= b

print_first(less_than, 25, 10)