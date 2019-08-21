"""
414. Third Maximum Number
Category: array
Difficulty: Ease

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

"""

class Solution(object):
    def thirdMaximumNumber(self, nums):
        first_max = float('-inf')
        second_max = float('inf')
        third_max = float('inf')

        for i in set(nums):
            if i >= first_max:
                third_max = second_max
                second_max = first_max
                first_max = i
            elif i >= second_max:
                third_max = second_max
                second_max = i
            elif i >= third_max:
                third_max = i
        if len(set(nums)) < 3:
            return first_max
        else:
            return third_max

if __name__ == "__main__":
    print(Solution().thirdMaximumNumber([3, 2, 1]))
    print(Solution().thirdMaximumNumber([2,1]))
    print(Solution().thirdMaximumNumber([2, 2, 3, 1]))





