"""
217. Contain Duplicate
Category: Array
Difficulty: Easy

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

"""

class Solution(object):
    def containDuplicate(self, nums):
        l = len(nums)
        nums.sort()
        for i in range(l-1):
            if nums[i] == nums[i+1]:
                return True
        return False

if __name__ == "__main__":
    print(Solution().containDuplicate([1,1,1,3,3,4,5,4,2,4,2]))
    print(Solution().containDuplicate([1,2,3,4]))