"""
594. Longest Harmonious Subsequence
Category: Hash table
Difficulty: Easy
"""
"""
We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
 

Note: The length of the input array will not exceed 20,000.
"""
import collections
class Solution(object):
    def findHS(self, nums):
        lookup = collections.Counter(nums)
        result = 0
        for i in lookup.keys():
            if i+1 in lookup:
                result = max(result, lookup[i]+lookup[i+1])

        return result

nums = [1,3,2,2,5,2,3,7]
if __name__ == "__main__":
    print(Solution().findHS(nums))