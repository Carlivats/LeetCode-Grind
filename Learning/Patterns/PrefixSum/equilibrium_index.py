# Finding Equilibrium Index - Medium
# An index i is called an equilibrium index if the sum of elements to the left of i is equal to the sum of elements on thr rigth of i
# Find all such indices in an array
"""
ex:
Input: nums = [-7,1,5,2,-4,3,0]
Output: [3,6]
"""
def find_equilibrium_index(arr):
    prefixSumUp = arr[:]
    for i in range(1,len(arr)):
        prefixSumUp[i] += prefixSumUp[i-1]
    print(prefixSumUp)

    prefixSumDown = arr[::-1]
    for i in range(1,len(arr)):
        prefixSumDown[i] += prefixSumDown[i-1]
    print(prefixSumDown)

arr = [-7,1,5,2,-4,3,0]
find_equilibrium_index(arr)