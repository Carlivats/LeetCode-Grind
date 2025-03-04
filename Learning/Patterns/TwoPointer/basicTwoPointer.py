# Basic Two Pointer (Opposite Direction)
# Given a sorted array of integers, find two numbers such that they add up to a specific target number.
# Return the indices of the two numbers
"""ex:
input: nums = [2,7,11,15], target = 9
output: [0,1] because nums[0] + nums[1] = 9
"""

def two_pointers(nums, target):
    left = 0
    right = len(nums)-1 # Initialize the pointers

    while left < right: # While left is smaller than right (They haven't crossed)
        if nums[left] + nums[right] == target:
            return [left,right] # If the numbers add up then return those
        elif nums[left] + nums[right] < target:
            left+=1
        else:
            right -=1
    return []



def test_two_pointers():
    test_cases = [
        # Test Case 1: Basic example
        {"input": ([2, 7, 11, 15], 9), "expected": [0, 1]},
        
        # Test Case 2: No solution
        {"input": ([1, 2, 3, 4], 10), "expected": []},
        
        # Test Case 3: Multiple valid pairs (return the first one)
        {"input": ([1, 2, 3, 4, 5], 7), "expected": [1, 4]},
        
        # Test Case 4: Negative numbers
        {"input": ([-3, -1, 0, 2, 5], -1), "expected": [0, 3]},
        
        # Test Case 5: Single element (no solution)
        {"input": ([5], 5), "expected": []},
        
        # Test Case 6: Empty array
        {"input": ([], 0), "expected": []},
    ]
    
    for i, test_case in enumerate(test_cases):
        nums, target = test_case["input"]
        expected = test_case["expected"]
        result = two_pointers(nums, target)
        
        assert result == expected, (
            f"Test Case {i + 1} Failed: "
            f"Input: {nums}, Target: {target}, "
            f"Expected: {expected}, Got: {result}"
        )
    
    print("All test cases passed!")

# Run the test function
test_two_pointers()