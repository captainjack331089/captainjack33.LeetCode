"""
189. Rotate Array
Category: Array
Difficulty: Easy

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]

Input: [1,2,3,4,5,6,7] and k = 5
Output: [3,4,5,6,7,1,2]

Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


"""
class Solution(object):
    def rotateArray(self, nums, k):
        n = len(nums)
        k = k % n

        nums[ :k], nums[k: ] = nums[(n-k): ], nums[ :(n-k)]

        return nums

if __name__ == "__main__":
    print(Solution().rotateArray([1,2,3,4,5,6,7], 3))
    print(Solution().rotateArray([1, 2, 3, 4, 5, 6, 7], 5))