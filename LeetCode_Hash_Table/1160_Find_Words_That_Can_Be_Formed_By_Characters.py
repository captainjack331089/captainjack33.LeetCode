"""
1160. Find Words that can be formed by characters
Category: Hash Table
Difficulty: Easy
"""
"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.
"""
import collections
class Solution(object):
    def countCharacters(self,words,chars):
        lookupc = collections.Counter(chars)
        result = 0

        for word in words:
            lookupw = collections.Counter(word)
            for c,i in lookupw.items():
                temp = 0
                if lookupc[c] < i:
                    temp += 1
                    break
            if temp == 0:
                result += len(word)

        return result



words = ["hello","world","leetcode"]
chars = "welldonehoneyr"

if __name__ == "__main__":
    print(Solution().countCharacters(words,chars))