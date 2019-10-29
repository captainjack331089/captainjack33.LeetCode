"""
7. Reverse an Integer
Category: Math
Difficulty: Easy
"""
"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
class Solution(object):
    def reverse(self, x):
        num = 0
        a = abs(x)

        while a != 0:
            temp = a % 10
            num = num * 10 + temp
            a //= 10
        if x >= 0 and num < (2 ** 31 - 1):
            return num
        elif x < 0 and num <= (2 ** 31 - 1):
            return -num
        else:
            return 0

if __name__ == "__main__":
    print(Solution().reverse(-123))