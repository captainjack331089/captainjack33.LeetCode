"""
268. Missing Numbers
Category: Array
Difficulty: Easy


Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

"""

class Solution(object):
    def missingNumber(self,nums):
        sums = sum(nums)
        length_origin = len(nums) + 1

        start = 0
        end = len(nums)

        return int((start + end) * length_origin / 2 - sums)


print(Solution().missingNumber([3,0,1]))
print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))
print(Solution().missingNumber([0,1]))