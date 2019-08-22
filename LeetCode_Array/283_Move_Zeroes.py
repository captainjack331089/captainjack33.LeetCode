"""
283. Move Zeroes
Category: Array
Difficulty: Easy

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.


"""

class Solution(object):
    def moveZeroes(self, nums):

        index = 0

        for i in range(len(nums)):
            if nums[i]:
                nums[index] = nums[i]
                index += 1
        for i in range(index, len(nums)):
            nums[i] = 0

        return nums








if __name__ == "__main__":
    print(Solution().moveZeroes([0,1,0,3,12]))