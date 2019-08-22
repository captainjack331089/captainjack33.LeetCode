"""
Category: Array
Difficulties: Easy

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
class Solution(object):
    def maximumArray(self,nums):
        if max(nums) < 0:
            return max(nums)

        local_max = 0
        global_max = 0
        for i in nums:
            local_max = max(0, i + local_max)
            #1,3,0,0,0,2,1,5,0
            global_max = max(local_max, global_max)
            #1,3,3,3,3,3,3,5,5
        return global_max


if __name__ == "__main__":

    print(Solution().maximumArray([1, 2, -3, -4, -1, 2, -1, 4, -5]))
    print(Solution().maximumArray([-1, -2, -3, -4, -2, -5]))
