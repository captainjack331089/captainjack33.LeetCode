"""
561. Array Partition I
Category: Array
Difficulty: Easy


Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].


"""

"""
思路： 这道题求一个数组中 任意两两一对的最小值的最大值。
其实通过计算：
数组：[a1,a2,...,b1,b2,...,ai,bi]
min(a1,b1)+...+min(ai,bi) 相当于sum = (a1+...+ai+b1+...+bi) - (abs(a1-b1)+...+abs(ai-bi))
(a1+...+ai+b1+...+bi)不会变,就是求 abs(a1-b1)+...+abs(ai-bi) 这个代数式的最小值，
通过研究发现， 最小值就是经过排序的数组相邻两个数字的差永远最小

"""
class Solution(object):
    def arrayPartitionI(self,nums):
        nums.sort()
        return (sum(nums[::2]))

print(Solution().arrayPartitionI([1,4,3,2]))