# Insertion Sort:   -   O(n^2)
# Inserst each elemtn into its correct position.
# This will sort it going up

def insertion_sort(arr):
    for i in range(1,len(arr)): # We check the whole arr
        temp = arr[i]           # We keep the current element
        j = i -1                # We keep the previous value in j, and its -1 because we assume that i and j are already sorted
        while j >= 0 and arr[j] > temp: # While j value is within our bounds and the prev is bigger than then curr...
            arr[j + 1] = arr[j]         # We make the first value the next one
            j -= 1                      # We make j go behind so it can compare with the previous
        arr[j+1] = temp                 # We set the value to switch with the temp


def insertion_test(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i -1
        while j >=0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

arr = [5,3,8,6,2,4323,245432,34567,9854,1234,1]
insertion_test(arr)
print(arr)

# Make an insertion Method.
# This is used to sort an array, and works best for small data

def insertion_practice(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i-1
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j-=1
        arr[j + 1] = temp

arr = [5,3,8,6,2,4323,245432,34567,9854,1234,1]
insertion_practice(arr)
print(arr)