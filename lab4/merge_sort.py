import numpy as np
import time
arr = numpy.random.randint(100, size=(10))

def merge_sort(arr):
    global count
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    count += 1
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


print("Before sorting array elements are - ")  
print(arr)  
count = merge_sort(arr)  
print("\nAfter sorting array elements are - ")  
print(arr)
print("\nNumber of iterations: ", count)
print("\nTime taken: ", time.time() - start_time)
