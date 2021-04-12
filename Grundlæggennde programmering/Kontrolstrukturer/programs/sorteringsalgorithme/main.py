import numpy as np
from numpy import array

def sort(array_input):
    leftovers = array([])
    new_array = array([array_input[0]])
    for x in array_input:
        if x < new_array[0]:
            new_array=np.insert(new_array,0,x)
            continue
        if x > new_array[-1]:
            new_array = np.insert(new_array, len(new_array),x)
            continue
        elif x not in leftovers and x != array_input[0]:
            print(x)
            leftovers = np.insert(leftovers, 0, int(x))
    for y in leftovers:
        for i in new_array:
            print(new_array.tolist().index(i))
            if y < i and y > new_array[new_array.tolist().index(i)-1]:
                new_array = np.insert(new_array, new_array.tolist().index(i),y)

    print(leftovers)
    print(new_array)

array_input_var = ([20, 10, 12, 8, 6, 4, 3, 1, 64535])
sort(array_input_var)