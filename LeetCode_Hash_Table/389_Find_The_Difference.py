"""
389. Find the Difference
Category: Hash Table
Difficulty: Easy
"""
"""
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
"""
import collections
class Solution(object):
    def findDifference(self,s,t):
        lookups = collections.Counter(s)
        lookupt = collections.Counter(t)

        for i,char in enumerate(t):
            if char not in s:
                return char
            elif lookups[char] != lookupt[char]:
                return char

s = "abcd"
t = "abcde"
s1 = "aaa"
t1 = "aaaa"

if __name__ == "__main__":
    print(Solution().findDifference(s,t))
    print(Solution().findDifference(s1, t1))