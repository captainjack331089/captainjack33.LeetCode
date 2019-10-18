"""
1189. Maximum Number of Balloons
Category: Hash Table
Difficulty: Easy
"""
"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 10^4
text consists of lower case English letters only.
"""
import collections
class Solution(object):
    def maxNumberOfBalloons(self, text):
        result = float("inf")

        balloon = collections.Counter("balloon")
        lookup = collections.Counter(text)
        for c,i in balloon.items():
            if lookup[c] < i:
                result = 0
                break
            else:
                temp = lookup[c] // i
                result = min(result,temp)
        return result



text = "loonbalxballpoon"

if __name__ == "__main__":
    print(Solution().maxNumberOfBalloons(text))