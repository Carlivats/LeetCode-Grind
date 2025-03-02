# Merge Sort    -   O(n log n)
# Divide the array into halves, sort each half, and then merge back

def merge_sort(arr):
    if len(arr) > 1:        # If the array is at least 2
        mid = len(arr) // 2 # We select the middle with "//" Because that will always be int
        left = arr[:mid]    # We choose the left side
        right = arr[mid:]   # We choose the right side

        merge_sort(left)    # Since we want to do this same thing with the rest, we call the left...
        merge_sort(right)   # and right
        i = 0
        j = 0   # could do i = j = k = 0 but this makes more sense
        k = 0

        # Main Algorithm
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j+= 1
            k+=1
        #If there is any elements of L[]
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        
        # there is any elements of R[]
        while j < len(right):
            arr[k] = right[j]
            i+=1
            j+=1



def merge_test(arr):
    if len(arr) > 1:
        m = len(arr) // 2 # m for medium
        L = arr[:m]
        R = arr[m:]

        merge_test(L)
        merge_test(R)

        i,j,k = 0,0,0                       # Looping Values
        while i < len(L) and j < len(R):    # i is for L and j is for R
            if L[i] < R[j]:                 # Where we actually compare two items
                arr[k] = L[i]               # On the first scenario we put the value k to the left
                i += 1
            else:
                arr[k] = R[j]               # On the second scenario we put the value k on right
                j += 1
            k+=1
        
        while i<len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j<len(R):
            arr[k] = R[j]
            j+=1
            k += 1




def mergesort_practice(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        left = arr[:m]
        right = arr[m:]

        mergesort_practice(left)
        mergesort_practice(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = [2,4,1,8,6,3]
mergesort_practice(arr)
print(arr)