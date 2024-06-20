# sliding window

"""
Given a list of integers num_list and a sliding window of size k that moves from left to right. 
Each time it moves 1 position to the right, you can see k numbers in num_list and find the largest 
number among these k numbers after each slide. k must be greater than or equal to 1.

Input: num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1] with k=3
Output: [5, 5, 5, 5, 10, 12, 33, 33]

"""


def sliding_window(nums, k):
    if k < 1:
        return []

    result = []
    for i in range(len(nums) - k + 1):
        window = nums[i:i + k]
        result.append(max(window))

    return result

# testing


nums = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 2
result = sliding_window(nums, k)
print(result)
