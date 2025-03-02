# Quick Sort
# in the worst case scenario is O(n^2), but it can be O(n log n) or go faster

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    # We select the pivot on the middle
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]    # We fill the left side
    middle = [x for x in arr if x == pivot] 
    right = [x for x in arr if x > pivot] 

    return quicksort(left) + middle + quicksort(right)


def quicksort_test(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort_test(left) + middle + quicksort_test(right)



def quicksort_practice(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort_practice(left) + middle + quicksort_practice(right)

arr = [2,4,1,8,6,3]
print(quicksort_practice(arr))