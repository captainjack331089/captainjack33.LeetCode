"""
771. Jewels And Stones
Category: Hash Table
Difficulty: Easy
"""
"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""
import collections
class Solution(object):
    def numJewelsInStones1(self, J, S):

        lookupS = collections.Counter(S)
        result = 0
        for j in J:
            result += lookupS[j]
        return result
    def numJewelsInStones2(self,J,S):

        return sum(S.count(j) for j in J)


J = "aA"
S = "aAAbbbb"

if __name__ == "__main__":
    print(Solution().numJewelsInStones1(J,S))
    print(Solution().numJewelsInStones2(J, S))