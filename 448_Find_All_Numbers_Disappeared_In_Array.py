"""

448. Find All Numbers Disappeared in Array
Category: Array
Difficulty: Easy

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]


"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        lookup = {}
        for i in range(1, len(nums)+1):
            lookup[i] = 0
        for i in range(len(nums)):
            lookup[nums[i]] += 1
        result = []
        for i in range(1,len(nums)):
            if lookup[i] == 0:
                result.append(i)
        return result

if __name__ == "__main__":
    print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))