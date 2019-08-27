"""
697. Degree of an Array
Category: Array
Difficulty: Easy

"""
"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

"""

class Solution(object):
    def degreeOfAnArray(self,nums):
        lookup_start = {}
        lookup_end = {}
        lookup_count = {}
        max_count = float('-inf')
        for i,num in enumerate(nums):
            if num not in lookup_start:
                lookup_start[num] = i
                lookup_count[num] = 0
            lookup_end[num] = i
            lookup_count[num] += 1
            max_count = max(max_count, lookup_count[num])

        min_d = float('inf')
        for num,count in lookup_count.items():
            if count == max_count:
                min_d = min(min_d, lookup_end[num]-lookup_start[num]+1)
        return min_d




if __name__ == "__main__":
    print(Solution().degreeOfAnArray([1,2,2,3,1]))
    print(Solution().degreeOfAnArray([1,2,2,3,1,4,2]))