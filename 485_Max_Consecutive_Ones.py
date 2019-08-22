"""
485. Max Consecutive Ones
Category: Array
Difficulty: Easy

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000


"""

class Solution(object):
    def maxConsecutiveOnes(self, nums):

        reserved_max = 0
        count = 0

        for i in nums:
            if i != 1:
                reserved_max = count
                count = 0
            else:
                count += 1
        return max(count, reserved_max)

if __name__ == "__main__":
    print(Solution().maxConsecutiveOnes([1,1,0,1,1,1,0]))