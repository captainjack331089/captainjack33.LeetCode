"""
643. Maximum Average SubArray I
Category: Array
Difficulty: Easy

"""

"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
 

Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].

思路：
找到最大平均值就是找到最大的sum
所以只要一直去 --》数组里k个连续数组的最大值 --》 遍历数组到k之后， 每次减去[k-i]对应位置的值

"""
class Solution(object):
    def findMaxAverage(self, nums, k):
        temp_sum = 0
        max_sum = float('-inf')

        for i in range(len(nums)):
            temp_sum += nums[i]
            if i == k-1:
                max_sum = temp_sum
            if i >= k:
                temp_sum = temp_sum - nums[k-i]
                max_sum = max(max_sum, temp_sum)

        return float(max_sum)/k

if __name__ == "__main__":
    print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))


