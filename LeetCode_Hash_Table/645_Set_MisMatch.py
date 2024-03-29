"""
645. Set MisMatch
Category: HashTable
Difficulty: Easy
"""
"""
The set S originally contains numbers from 1 to n. 
But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, 
which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. 
Your task is to firstly find the number occurs twice and then find the number that is missing. 
Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
"""
import collections
class Solution(object):
    def findErrorNums(self,nums):
        result = []
        lookup = collections.Counter(nums)
        le = len(nums)
        for i in set(nums):
            if lookup[i] > 1:
                result.append(i)
                result.append(int(  (1+le)*le/2 - (sum(nums)-i)   ))
        return result


nums = [1,2,2,4]
if __name__ == "__main__":
    print(Solution().findErrorNums(nums))