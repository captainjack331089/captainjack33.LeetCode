"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""

class Solution(object):
    def plusOne(self,digits):

        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        #9999
        digits[0] = 1
        digits.append(0)
        return digits


if __name__== "__main__":
    print(Solution().plusOne([1, 2, 3]))
    print(Solution().plusOne([4, 3, 2, 1]))
    print(Solution().plusOne([9, 9, 9, 9, 9]))

