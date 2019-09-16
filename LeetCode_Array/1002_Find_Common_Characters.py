"""
1002. Find Common Characters
Category: Array
Difficulty: Easy
"""
"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
Accepted
37,179
Submissions
56,607
"""
import collections
class Solution(object):
    def findCommonCharacters(self,A):
        lookup = collections.Counter(A[0])
        for i in range(1,len(A)):
            lookup &= collections.Counter(A[i])
        return (list(lookup.elements()))

if __name__ == "__main__":
    print(Solution().findCommonCharacters(["bella","label","roller"]))