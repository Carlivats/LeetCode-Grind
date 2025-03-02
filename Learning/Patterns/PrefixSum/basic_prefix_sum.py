# Basic Prefix Sum Calculation
# Given and array [nums], return a new array prefixsum where prefix_sum[i] is the sum of the elements from nums[0] to nums[i]

def basic_prefix_sum(arr):
    if arr == 0:
        return arr
    for i in range(1,len(arr)):
        arr[i] = arr[i] + arr[i-1]
    prefixSum = arr
    return prefixSum

arr = [1, 2, 3, 4]
print(basic_prefix_sum(arr))