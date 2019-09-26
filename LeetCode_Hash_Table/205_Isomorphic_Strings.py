"""
205. Isomorphic Strings
Category: Hash Table
Difficulty: Easy
"""
"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""

class Solution(object):
    def isIsomorphic(self,s,t):

        return (self.isomorphic(s,t) and self.isomorphic(t,s))

    def isomorphic(self,s,t):
        lookup = {}
        for i in range(len(s)):
            if s[i] not in lookup:
                lookup[s[i]] = t[i]
            elif lookup[s[i]] != t[i]:
                return False
        return True

s = "paper"
t = "title"

s2 = "paper"
t2 = "admin"
if __name__ == "__main__":
    print(Solution().isIsomorphic(s,t))
    print(Solution().isIsomorphic(s2,t2))