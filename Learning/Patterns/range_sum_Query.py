# Range Sum Query (Static Queries)  - Easy-Medium
# Given an array [nums], answer multiple queries of the form (left, right), where you need to find the sum of elements in the range [left, right]
"""ex:
Input: nums = [3, 6, 2, 8, 7]  
Queries: [(1, 3), (0, 2)]  
Output: [16, 11]  
Explanation:  
Sum from index 1 to 3 → 6 + 2 + 8 = 16  
Sum from index 0 to 2 → 3 + 6 + 2 = 11  
"""

def range_sum_query(arr,query):
    prefixSum = [0] * len(query)


    for i in range(len(prefixSum)):
        left = query[i][0] + 1
        right = query[i][1] + 1
        #print(f"{i}:{left} ; {i}:{right}")
        if query[1] == 0:
            return arr[right]
        
        tempArr = arr[:]
        for j in range(left,right):
            #print(tempArr)
            tempArr[j] = tempArr[j] + tempArr[j-1]
        #print(tempArr)
        prefixSum[i] = tempArr[right-1]
    return prefixSum

nums = [3, 6, 2, 8, 7]
quieries = [(1, 3), (1, 2)]
print(range_sum_query(nums,quieries))
