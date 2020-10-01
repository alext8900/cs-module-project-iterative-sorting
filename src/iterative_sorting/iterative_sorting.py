import atexit
from time import time, strftime, localtime
from datetime import timedelta

def secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))

def log(s, elapsed=None):
    line = "="*40
    print(line)
    print(secondsToStr(), '-', s)
    if elapsed:
        print("Elapsed time:", elapsed)
    print(line)
    print()

def endlog():
    end = time()
    elapsed = end-start
    log("End Program", secondsToStr(elapsed))
print("First timed program")
start = time()
log("Start Program")

# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index            
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
    
        # TO-DO: swap
        # Your code here
        
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr

# Verifying it works
random_list_of_numbers = [1, 10, 7, 8, 2, 23, 6]
selection_sort(random_list_of_numbers)
print(random_list_of_numbers)
atexit.register(endlog)

# TO-DO:  implement the Bubble Sort function below
start = time()
def bubble_sort(arr):
    # we set swapped to true so the loop runs at least Once
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
            # Swap the elements
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            # Set the flag to true so we'll loop again
                swapped = True
            
    return arr

# Verify it works
log("Initiate bubble sort")
random_list_of_numbers1 = [4, 7, 2, 30, 12, 10, 9, 22]
bubble_sort(random_list_of_numbers1)
print(random_list_of_numbers1)
atexit.register(endlog)

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
# i tried
def counting_sort(arr, maximum=None):
    if len(arr) == 0:
        return arr
    if maximum is None:
        maximum = max(arr)
    
    buckets = [0 for i in range(maximum + 1)] 

    for value in arr:
        if value < 0:
            return "Error, negative numbers not allowed in Count Sort."
        buckets[value] += 1
        
    output = []
    
    for index, count in enumerate(buckets):
        output.extend([index for i in range(count)])
        
    return output
    
