"""
387. First Unique character in a string
Category: Hash-Table
Difficulty: Easy
"""
"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.


"""
import collections

class Solution(object):
    def firstUniqueChar(self,s):
        count = collections.Counter(s)
        for index,char in enumerate(s):
            if count[char] == 1:
                return index
        return -1


s = "loveleetcode"
if __name__ == "__main__":
    print(Solution().firstUniqueChar(s))