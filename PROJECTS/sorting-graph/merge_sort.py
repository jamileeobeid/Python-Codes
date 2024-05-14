import array as arr

def split(array):
    evens = arr.array('i', [0] * (len(array)//2))
    odds = arr.array('i', [0] * (len(array)//2))
    c1 = 0
    c2 = 0
    for i in range(len(array)):
        if i % 2 == 0:
            if c1 < len(evens):
                evens[c1] = array[i]
                c1 += 1
        else:
            if c2 < len(odds):
                odds[c2] = array[i]
                c2 += 1
    return evens, odds

def merge(half1, half2):
    result = arr.array('i', [0] * (len(half1) + len(half2)))
    i1 = 0
    i2 = 0
    index = 0

    while i1 < len(half1) and i2 < len(half2):
        if half1[i1] <= half2[i2]:
            result[index] = half1[i1]
            i1 += 1
        else:
            result[index] = half2[i2]
            i2 += 1
        index += 1

    while i1 < len(half1):
        result[index] = half1[i1]
        i1 += 1
        index += 1

    while i2 < len(half2):
        result[index] = half2[i2]
        i2 += 1
        index += 1

    return result

def merge_sort(a):
    if len(a) <= 1:
        return a
    else:
        half1, half2 = split(a)
        half1 = merge_sort(half1)
        half2 = merge_sort(half2)
        merged = merge(half1, half2)
        return merged
