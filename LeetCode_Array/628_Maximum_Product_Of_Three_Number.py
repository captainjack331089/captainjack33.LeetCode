"""

628. Maximum Product of three Number
Category: Array
Difficulty: Easy

"""

"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6
 

Example 2:

Input: [1,2,3,4]
Output: 24
 

Note:

The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""

class Solution(object):
    def maximumProduct(self, nums):
        nums = sorted(nums)
        all_positive = nums[-1]*nums[-2]*nums[-3]
        two_negative = nums[-1]*nums[0]*nums[1]
        return (max(all_positive, two_negative))

if __name__ == "__main__":
    print(Solution().maximumProduct([1,2,3,4]))
    print(Solution().maximumProduct([-6, 1, 2, 3, 4]))
    print(Solution().maximumProduct([-7, -5, 1, 2, 3, 4]))