def maxSum(arr,k):
    n = len(arr)
    windowSum = max(arr[:k])
    maxSum = windowSum
    for i in range(k,n):
        windowSum = windowSum + arr[i] - arr[i-k]
        maxSum = max(maxSum,windowSum)
    
    return maxSum / k

def maxSum_test(arr,k):
    n = len(arr)
    windowSum = max(arr[:k])
    maxSum = windowSum
    for i in range(k,n):
        windowSum = windowSum - arr[i-k] + arr[i]
        if maxSum < windowSum:
            maxSum = windowSum
    return maxSum / k