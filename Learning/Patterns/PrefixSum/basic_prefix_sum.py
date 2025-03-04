# Basic Prefix Sum Calculation  - Easy 
# Given and array [nums], return a new array prefixsum where prefix_sum[i] is the sum of the elements from nums[0] to nums[i]

def basic_prefix_sum(arr):
    prefixSum = [0]* len(arr)
    prefixSum[0] = arr[0]
    for i in range(1,len(arr)):
        prefixSum[i] = prefixSum[i-1] + arr[i]
    return prefixSum

arr = [1, 2, 3, 4]
print(basic_prefix_sum(arr))