"""LeetCode Problem

Category: Array
Difficulty: Easy
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same elemetn twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + num[1] = 2 + 7 = 9,
return [0, 1].

"""



import time

nums = [1, 2, 4, 6, 7, 9, 12, 21]
target = 18


class Solution(object):

    """Method 1:
       Using the most stupid way to solve
    """
    def twoSum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        result = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result

    """Method2:
        Using the Hash way to seperate numbers
    """

    def twoSum2(self, nums, target):
        result = {}
        for i in range (len(nums)):
            remain_value = target - nums[i]
            if remain_value not in result:
                result[nums[i]] = i
            else:
                return [result[remain_value],i]

    """
    Method3:
        Using enumerate import from python in literate
    """

    def twoSum3(self, nums, target):
        result = {}
        for i, j in enumerate(nums):
            remain_value = target - j
            if remain_value not in result:
                result[j] = i
            else:
                return [result[remain_value], i]


if __name__ == "__main__":
    t0 = time.time()
    solution = Solution()
    #print(solution.twoSum(nums,target))
    #print(time.time()-t0)
    # print(solution.twoSum2(nums,target))
    # print(time.time()-t0)
    print(solution.twoSum3(nums, target))
    print(time.time()- t0)











