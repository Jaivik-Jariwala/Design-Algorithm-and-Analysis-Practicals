import numpy
arr = numpy.random.randint(10, size=(100000))
import time
start_time = time.time()

def insertion_sort(arr):
    count = 0
    for i in range(0,len(arr)):
        val=arr[i]
        j=i-1
        while j>=0 and val<arr[j]:
            arr[j+1] = arr[j]
            j-=1
            count+=1
        arr[j+1]=val
    return(arr, count)

end_time =time.time()
compilation_time = end_time - start_time

print("unsorted array is : " ,arr)
arr, count = insertion_sort(arr)
end_time =time.time()
compilation_time = end_time - start_time

print("sorted array is : " ,arr)
print("number of times loop : ",count)
print("compilation time : ",compilation_time)
