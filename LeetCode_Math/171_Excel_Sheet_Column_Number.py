"""
171. Excel Sheet Column Number
Category: Math
Difficulty: Easy
"""
"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""

class Solution():
    def titleToNumber(self, s):

        result = 0
        for i in range(len(s)):
            result *= 26
            result += ord(s[i]) - ord('A') + 1
        return result

s1 = 'AA'
s2 = 'CD'

if __name__ == "__main__":
    print(Solution().titleToNumber(s1))
    print(Solution().titleToNumber(s2))