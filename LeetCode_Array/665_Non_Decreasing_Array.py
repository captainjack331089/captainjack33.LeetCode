"""
665. Non Decreasing Array
Category: Array
Difficulty: Easy

"""

"""
665. Non-decreasing Array

Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].

思路：就是拿数组里面找到对应坐标[i]>[i+1]的点。 
     判断这个点是不是唯一点
     那就要考虑： 1： 初始点
                2： 倒数第二个点
                3： 相邻点
"""

class Solution(object):
    def checkPossibility(self, nums):
        p = None
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if p is not None:
                    return False
                p = i

        return (p==0 or p==len(nums)-2 or nums[p+1]>=nums[p-1] or nums[p+2]>=nums[p])

if __name__ == "__main__":
    print(Solution().checkPossibility([4,2,3]))
    print(Solution().checkPossibility([5, 10, 9, 8, 12]))
