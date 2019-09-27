"""
290. Word Pattern
Category: Hash Table
Difficulty: Easy
"""
"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
"""
class Solution(object):
    def wordPattern(self,pattern,str):
        words = str.split(' ')
        if len(words) != len(pattern):
            return False
        lookup1 = {}
        lookup2 = {}

        for i in range(len(pattern)):
            if pattern[i] in lookup1:
                if lookup1[pattern[i]] != words[i]:
                    return False

            else:
                if words[i] in lookup2:
                    return False
                lookup1[pattern[i]] = words[i]
                lookup2[words[i]] = True
        return True


pattern = "abba"
str = "dog cat cat dog"

if __name__ == "__main__":
    print(Solution().wordPattern(pattern,str))