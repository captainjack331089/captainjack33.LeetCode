"""
581. Shortest Unsorted Continuous Array
Category: Array
Difficulty: Easy
"""
"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.

"""
class Solution(object):
    def findUnsortedSubarray(self, nums):
        new_nums = sorted(nums)
        length = len(nums) - 1

        if nums == new_nums:
            return 0

        max_index = length
        min_index = 0

        for i in range(length):
            if nums[i] != new_nums[i]:
                min_index = i
                break
        for i in range(length, 0, -1):
            if nums[i] != new_nums[i]:
                max_index = i
                break
        return (max_index - min_index + 1)


print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))

