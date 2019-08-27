"""
674. Longest Continuous Increasing Subsequence
Category: Array
Difficulty Easy
"""
"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
Note: Length of the array will not exceed 10,000.

"""
class Solution(object):
    def findLengthOfLCIS(self,nums):
        max_l = 0
        index = 0

        #写法1：
        if len(nums) == 1:
            return 1
        for i in range(1,len(nums)):
            if nums[i-1] >= nums[i]: #写法2： if i and ...
                index = i

            max_l = max(max_l, i-index+1)
        return max_l

if __name__ == "__main__":
    print(Solution().findLengthOfLCIS([1,3,5,4,7]))