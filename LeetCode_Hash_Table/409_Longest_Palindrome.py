"""
409. Longest Palindrome
Category: Hash Table
Difficulty: Easy
"""
"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

import collections

class Solution(object):
    def longestPlindrome(self,s):
        result = 0
        for count in collections.Counter(s).values():
            result += count // 2 * 2
            if result % 2 == 0 and count % 2 == 1:
                result += 1

        return result



s = 'abccccdd'

print(Solution().longestPlindrome(s))