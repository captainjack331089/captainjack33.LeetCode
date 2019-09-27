"""
242. Valid Anagram
Category: Hash Table
Difficulty: Easy
"""
"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
import builtins
class Solution(object):
    def isAnagram(self,s,t):

        lookup1 = {}
        lookup2 = {}

        for i in s:
            lookup1[i] = lookup1.get(i,0) + 1
        for j in t:
            lookup2[j] = lookup2.get(j,0) + 1

        return lookup1 == lookup2




s = "anagram"
t = "nagaram"
if __name__ == "__main__":
    print(Solution().isAnagram(s,t))
